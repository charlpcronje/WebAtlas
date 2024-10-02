import pytest
from webatlas.config.config_manager import ConfigManager

def test_config_manager_initialization():
    config_manager = ConfigManager()
    assert isinstance(config_manager, ConfigManager)

def test_config_manager_get():
    config_manager = ConfigManager()
    assert config_manager.get("max_depth", 5) == 5