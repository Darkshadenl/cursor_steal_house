import asyncio
import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional

from crawler_job.models.pydantic_models import WebsiteScrapeConfigJson
from crawler_job.services.repositories.json_config_repository import (
    JsonConfigRepository,
)


class ConfigProvider(ABC):
    @abstractmethod
    async def get_config_async(
        self, website_name: str
    ) -> Optional[WebsiteScrapeConfigJson]:
        """Retrieve the configuration for the specified website."""
        raise NotImplementedError


class DbConfigProvider(ConfigProvider):
    def __init__(self, json_config_repository: JsonConfigRepository) -> None:
        self.json_config_repository = json_config_repository

    async def get_config_async(
        self, website_name: str
    ) -> Optional[WebsiteScrapeConfigJson]:
        return await self.json_config_repository.get_config_by_website_name_async(
            website_name
        )


class FileConfigProvider(ConfigProvider):
    def __init__(self, base_directory: Path) -> None:
        self.base_directory = base_directory

    async def get_config_async(
        self, website_name: str
    ) -> Optional[WebsiteScrapeConfigJson]:
        file_path = self._resolve_file_path(website_name)
        if not file_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found for website '{website_name}' at '{file_path}'."
            )

        file_content = await asyncio.to_thread(file_path.read_text, encoding="utf-8")
        try:
            config_data = json.loads(file_content)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Invalid JSON in configuration file '{file_path}': {exc}"
            ) from exc

        return WebsiteScrapeConfigJson.model_validate(config_data)

    def _resolve_file_path(self, website_name: str) -> Path:
        normalized_name = website_name.strip().lower().replace(" ", "_")
        file_name = f"{normalized_name}.json"
        return self.base_directory / file_name


class ConfigProviderFactory:
    DEFAULT_FILES_DIRECTORY = (
        Path(__file__).resolve().parents[2] / "config_sources" / "website_configs"
    )

    @classmethod
    def create_provider(
        cls,
        config_source: str,
        *,
        json_config_repository: Optional[JsonConfigRepository] = None,
        files_directory: Optional[Path] = None,
    ) -> ConfigProvider:
        normalized_source = config_source.strip().lower()
        if normalized_source == "db":
            if json_config_repository is None:
                raise ValueError(
                    "JsonConfigRepository is required when CONFIG_SOURCE is set to 'db'."
                )
            return DbConfigProvider(json_config_repository)

        if normalized_source == "files":
            target_directory = files_directory or cls.DEFAULT_FILES_DIRECTORY
            if not target_directory.exists():
                raise FileNotFoundError(
                    f"Configuration files directory '{target_directory}' does not exist."
                )
            return FileConfigProvider(target_directory)

        raise ValueError(
            f"Unsupported config source '{config_source}'. "
            "Allowed values are: db, files."
        )
