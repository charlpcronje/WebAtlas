import json
import os

class ConfigManager:
    def __init__(self, project_config_path=None):
        self.default_config = self._load_config("webatlas/config/default_config.json")
        self.project_config = self._load_config(project_config_path) if project_config_path else {}
        self.config = self._merge_configs()

    def _load_config(self, config_path):
        if not config_path or not os.path.exists(config_path):
            return {}
        with open(config_path, 'r') as config_file:
            return json.load(config_file)

    def _merge_configs(self):
        merged = self.default_config.copy()
        merged.update(self.project_config)
        return merged

    def get(self, key, default=None):
        return self.config.get(key, default)