import pytest
from webatlas.core.crawler_engine import CrawlerEngine
from webatlas.config.config_manager import ConfigManager

def test_crawler_engine_initialization():
    config_manager = ConfigManager()
    crawler_engine = CrawlerEngine(config_manager)
    assert isinstance(crawler_engine, CrawlerEngine)