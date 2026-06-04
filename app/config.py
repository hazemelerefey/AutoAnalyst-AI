"""Application configuration for AutoAnalyst AI Dashboard."""
import os
from dataclasses import dataclass, field


@dataclass
class AppConfig:
    host: str = "0.0.0.0"
    port: int = 8050
    debug: bool = False
    max_upload_size_mb: int = 100
    allowed_extensions: set[str] = field(default_factory=lambda: {".csv", ".xlsx", ".xls"})
    max_chart_points: int = 10_000
    cache_type: str = "FileSystemCache"
    cache_dir: str = ".cache"
    cache_timeout: int = 3600

    @property
    def max_upload_bytes(self) -> int:
        return self.max_upload_size_mb * 1024 * 1024


def get_config() -> AppConfig:
    return AppConfig(
        debug=os.getenv("DASH_DEBUG", "false").lower() == "true",
        port=int(os.getenv("PORT", "8050")),
    )
