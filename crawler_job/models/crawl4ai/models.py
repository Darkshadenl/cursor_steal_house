# crawl4ai_classes.py
from typing import List, Dict, Optional, Any, Union
from enum import Enum


class ExtractionType(str, Enum):
    BASIC = "basic"
    ARTICLE = "article"
    HTML2TEXT = "html2text"
    LANGCHAIN = "langchain"  # Corrected typo
    READABILITY = "readability"


class ChunkingType(str, Enum):
    STRING = "string"
    PARAGRAPH = "paragraph"
    SENTENCE = "sentence"


class ContentFilterType(str, Enum):
    BM25 = "bm25"
    JACCARD = "jaccard"
    COSINE = "cosine"


class CacheMode(str, Enum):
    ENABLED = "enabled"
    DISABLED = "disabled"
    READ_ONLY = "read_only"
    WRITE_ONLY = "write_only"
    BYPASS = "bypass"


class ExtractionConfig:
    def __init__(
        self, type: ExtractionType = ExtractionType.BASIC, params: Dict[str, Any] = None
    ):
        self.type: ExtractionType = type
        self.params: Dict[str, Any] = params or {}

    def to_dict(self) -> Dict[str, Any]:
        return {"type": self.type.value, "params": self.params}


class ChunkingStrategy:
    def __init__(
        self, type: ChunkingType = ChunkingType.STRING, params: Dict[str, Any] = None
    ):
        self.type: ChunkingType = type
        self.params: Dict[str, Any] = params or {}

    def to_dict(self) -> Dict[str, Any]:
        return {"type": self.type.value, "params": self.params}


class ContentFilter:
    def __init__(
        self,
        type: ContentFilterType = ContentFilterType.BM25,
        params: Dict[str, Any] = None,
    ):
        self.type: ContentFilterType = type
        self.params: Dict[str, Any] = params or {}

    def to_dict(self) -> Dict[str, Any]:
        return {"type": self.type.value, "params": self.params}


class CrawlerParams:
    def __init__(
        self,
        headless: bool = True,
        load_iframes: bool = False,
        load_images: bool = False,
        viewport_width: Optional[int] = None,
        viewport_height: Optional[int] = None,
        device_scale_factor: Optional[float] = None,
        user_agent: Optional[str] = None,
        proxy: Optional[str] = None,
        block_resources: Optional[List[str]] = None,
        timeout: Optional[int] = None,
        max_retries: Optional[int] = None,
        request_headers: Optional[Dict[str, str]] = None,
        wait_for_selector: Optional[str] = None,
        wait_for_timeout: Optional[float] = None,
        cookies: Optional[List[Dict[str, Any]]] = None,
        extra_headers: Optional[Dict[str, str]] = None,
    ):
        self.headless = headless
        self.load_iframes = load_iframes
        self.load_images = load_images
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height
        self.device_scale_factor = device_scale_factor
        self.user_agent = user_agent
        self.proxy = proxy
        self.block_resources = block_resources
        self.timeout = timeout
        self.max_retries = max_retries
        self.request_headers = request_headers
        self.wait_for_selector = wait_for_selector
        self.wait_for_timeout = wait_for_timeout
        self.cookies = cookies
        self.extra_headers = extra_headers

    def to_dict(self) -> Dict[str, Any]:
        # Filter out None values to keep the dictionary clean
        return {k: v for k, v in self.__dict__.items() if v is not None}


class CrawlRequest:
    def __init__(
        self,
        urls: Union[str, List[str]],  # Allow single URL or list
        word_count_threshold: int = 1,
        extraction_config: Optional[ExtractionConfig] = None,
        chunking_strategy: Optional[ChunkingStrategy] = None,
        content_filter: Optional[ContentFilter] = None,
        js_code: Optional[List[str]] = None,
        wait_for: Optional[str] = None,
        css_selector: Optional[str] = None,
        screenshot: bool = False,
        magic: bool = False,
        extra: Optional[Dict[str, Any]] = None,
        session_id: Optional[str] = None,
        cache_mode: CacheMode = CacheMode.ENABLED,
        priority: int = 5,
        ttl: int = 3600,
        crawler_params: Optional[CrawlerParams] = None,
    ):
        self.urls: List[str] = [urls] if isinstance(urls, str) else urls
        self.word_count_threshold: int = word_count_threshold
        self.extraction_config: Dict[str, Any] = (
            extraction_config.to_dict()
            if extraction_config
            else ExtractionConfig().to_dict()
        )  # Default
        self.chunking_strategy: Dict[str, Any] = (
            chunking_strategy.to_dict() if chunking_strategy else None
        )
        self.content_filter: Dict[str, Any] = (
            content_filter.to_dict() if content_filter else None
        )
        self.js_code: Optional[List[str]] = js_code
        self.wait_for: Optional[str] = wait_for
        self.css_selector: Optional[str] = css_selector
        self.screenshot: bool = screenshot
        self.magic: bool = magic
        self.extra: Optional[Dict[str, Any]] = extra
        self.session_id: Optional[str] = session_id
        self.cache_mode: str = cache_mode.value
        self.priority: int = priority
        self.ttl: int = ttl
        self.crawler_params: Dict[str, Any] = (
            crawler_params.to_dict() if crawler_params else {}
        )  # Allow empty

    def to_dict(self) -> Dict[str, Any]:
        # Filter out None values, but keep empty dicts/lists
        data = {
            k: v
            for k, v in self.__dict__.items()
            if v is not None or isinstance(v, (dict, list))
        }
        return data
