# webatlas/__main__.py

import argparse
from webatlas.config.config_manager import ConfigManager
from webatlas.core.crawler_engine import CrawlerEngine
from webatlas.utils.output_generator import OutputGenerator

def main():
    parser = argparse.ArgumentParser(description="WebAtlas: A versatile web crawler")
    parser.add_argument("--config", help="Path to the project-specific configuration file")
    args = parser.parse_args()

    config_manager = ConfigManager(args.config)
    crawler = CrawlerEngine(config_manager)
    output_generator = OutputGenerator(config_manager)
    
    print("Starting WebAtlas crawler...")
    print(f"Configuration: {config_manager.config}")
    crawler.start()
    
    print("Saving tree structure...")
    output_generator.save_tree_structure(crawler.get_tree_structure())
    print("Crawling completed.")

if __name__ == "__main__":
    main()