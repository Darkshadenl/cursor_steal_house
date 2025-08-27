from typing import Optional


class ConfigService:
    """Global configuration service using singleton pattern."""

    _instance: Optional["ConfigService"] = None
    _debug_mode: bool = False

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
        return cls._instance

    @property
    def debug_mode(self) -> bool:
        """Get the debug mode setting."""
        return self._debug_mode

    @debug_mode.setter
    def debug_mode(self, value: bool) -> None:
        """Set the debug mode setting."""
        self._debug_mode = value


# Global instance
config = ConfigService()
