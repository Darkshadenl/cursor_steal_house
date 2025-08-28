from crawler_job.flexibleCrawlers.base_scraper import ScrapeStrategy
from crawler_job.models.pydantic_models import WebsiteScrapeConfigJson
from crawler_job.services.logger_service import setup_logger

logger = setup_logger(__name__)


class WebsiteConfigValidator:
    def __init__(self, config: WebsiteScrapeConfigJson):
        self.config = config

    def validate(self) -> None:
        """Validate all website configuration requirements based on strategy."""
        if not self.config:
            raise Exception("Website configuration not provided")

        if not self.config.base_url:
            raise Exception("Base URL not provided in website configuration")

        if not self.config.strategy_config:
            raise Exception("Strategy configuration not provided")

        strategy = self.config.scrape_strategy

        if strategy == ScrapeStrategy.GALLERY.value:
            self._validate_gallery_config()
        elif strategy == ScrapeStrategy.SITEMAP.value:
            self._validate_sitemap_config()
        else:
            raise Exception(f"Unknown scrape strategy: {strategy}")

        self._validate_optional_configs()

        logger.info(
            f"Website configuration validation completed successfully for {self.config.website_name}"
        )

    def _validate_gallery_config(self) -> None:
        """Validate gallery extraction configuration."""
        if not self.config.strategy_config.gallery_extraction_config:
            raise Exception("Gallery extraction configuration not provided")

        gallery_config = self.config.strategy_config.gallery_extraction_config

        if not gallery_config.correct_urls_paths:
            raise Exception(
                "No correct URLs provided in gallery extraction configuration"
            )

        if not gallery_config.schema:
            raise Exception("No schema provided in gallery extraction configuration")

        if not gallery_config.schema_type:
            raise Exception(
                "No schema type provided in gallery extraction configuration"
            )

    def _validate_sitemap_config(self) -> None:
        """Validate sitemap extraction configuration."""
        if not self.config.strategy_config.sitemap_extraction_config:
            raise Exception("Sitemap extraction configuration not provided")

        sitemap_config = self.config.strategy_config.sitemap_extraction_config

        if not sitemap_config.regex:
            raise Exception("No regex provided in sitemap extraction configuration")

        if not sitemap_config.schema:
            raise Exception("No schema provided in sitemap extraction configuration")

    def _validate_optional_configs(self) -> None:
        """Validate optional configurations that may be required based on decorators usage."""
        detail_page_extraction_config = (
            self.config.strategy_config.detail_page_extraction_config
        )
        if (
            detail_page_extraction_config
            and detail_page_extraction_config.schema_type == "llm"
        ):
            if not detail_page_extraction_config.extra_llm_instructions:
                logger.warning(
                    "No extra LLM instructions provided for detail page extraction"
                )

        login_config = self.config.strategy_config.login_config
        if login_config and login_config.login_required:
            if not login_config.username_selector:
                raise Exception("Username selector not provided in login configuration")
            if not login_config.password_selector:
                raise Exception("Password selector not provided in login configuration")
            if not login_config.submit_selector:
                raise Exception("Submit selector not provided in login configuration")
