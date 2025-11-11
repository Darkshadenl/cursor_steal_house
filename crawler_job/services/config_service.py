import os
from typing import Optional


class ConfigService:
    """Global configuration service using singleton pattern."""

    _instance: Optional["ConfigService"] = None
    _debug_mode: bool = False
    _config_source: str = "db"
    _allowed_config_sources = {"db", "files"}

    def __new__(cls) -> "ConfigService":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def initialize(cls, debug_mode: bool = False) -> "ConfigService":
        """Initialize the configuration service with values."""
        if cls._instance is None:
            cls._instance = cls()
        cls._instance._debug_mode = debug_mode
        cls._instance._config_source = cls._load_config_source()
        return cls._instance

    @property
    def debug_mode(self) -> bool:
        """Get the debug mode setting."""
        return self._debug_mode

    @debug_mode.setter
    def debug_mode(self, value: bool) -> None:
        """Set the debug mode setting."""
        self._debug_mode = value

    @property
    def config_source(self) -> str:
        """Get the configured config source."""
        return self._config_source

    @config_source.setter
    def config_source(self, value: str) -> None:
        """Set the config source."""
        normalized_value = value.strip().lower()
        if normalized_value not in self._allowed_config_sources:
            raise ValueError(
                f"Invalid config source '{value}'. "
                f"Allowed values are: {', '.join(sorted(self._allowed_config_sources))}."
            )
        self._config_source = normalized_value

    @classmethod
    def _load_config_source(cls) -> str:
        value = os.getenv("CONFIG_SOURCE", "db").strip().lower()
        if value not in cls._allowed_config_sources:
            raise ValueError(
                f"Invalid CONFIG_SOURCE '{value}'. "
                f"Allowed values are: {', '.join(sorted(cls._allowed_config_sources))}."
            )
        return value


# Global instance
config = ConfigService()
