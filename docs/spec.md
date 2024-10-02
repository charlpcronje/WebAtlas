# WebAtlas Specification

## 1. System Overview

WebAtlas is a comprehensive web crawling and analysis tool designed to systematically browse websites, extract key information, and generate structured output. It offers flexibility through a configurable crawling engine, robust data extraction capabilities, and interactive visualizations.

## 2. System Components

1. **Configuration Manager**: Handles loading and merging of default and user-specified configurations.
2. **Crawler Engine**: Core component responsible for navigating web pages and managing the crawling process.
3. **Data Extractor**: Extracts relevant information from crawled pages.
4. **Output Generator**: Creates various output formats based on the crawled data.
5. **Graph Generator**: Builds a graph representation of the crawled website structure.
6. **Web Interface**: Provides a user-friendly way to configure and initiate crawls, and view results.

## 3. Key Files

1. `webatlas/__main__.py`: Main entry point for the crawler.
2. `webatlas/config/config_manager.py`: Manages configuration loading and merging.
3. `webatlas/core/crawler_engine.py`: Implements the core crawling logic.
4. `webatlas/core/data_extractor.py`: Contains methods for extracting data from web pages.
5. `webatlas/utils/output_generator.py`: Generates various output formats.
6. `crawler_config.html`: Web interface for configuring and starting crawls.
7. `start_crawler.php`: PHP script to handle form submission and execute the crawler.
8. `dashboard.html`: Interactive dashboard for viewing crawl results.

## 4. Data Flow

1. User inputs configuration via web interface or JSON file.
2. Configuration is processed by Configuration Manager.
3. Crawler Engine navigates web pages based on configuration.
4. Data Extractor pulls relevant information from each page.
5. Output Generator creates structured output files.
6. Graph Generator builds a representation of the site structure.
7. Results are displayed in the interactive dashboard.

## 5. Crawler Configuration Options

- `start_url`: Initial URL to begin crawling
- `max_depth`: Maximum depth of crawling
- `delay`: Time delay between requests (in seconds)
- `user_agent`: User agent string for requests
- `request_timeout`: Timeout for requests (in seconds)
- `max_retries`: Maximum number of retries for failed requests
- `exclude_patterns`: List of regex patterns for URLs to exclude
- `respect_robots_txt`: Whether to respect robots.txt rules
- `crawl_subdomains`: Whether to crawl subdomains
- `max_pages`: Maximum number of pages to crawl
- `follow_redirects`: Whether to follow redirects
- `save_html`: Whether to save HTML content of pages
- `create_sitemap`: Whether to generate a sitemap

## 6. Output Formats

1. JSON files for each crawled page
2. Tree structure of the crawled website (JSON)
3. Graph data for visualization (JSON)
4. List of broken links (JSON)
5. HTML content of pages (optional)
6. Sitemap (optional)

## 7. Web Interface

The web interface provides:
1. A form for inputting crawler configuration
2. Real-time progress updates during crawling
3. An interactive dashboard for exploring results

## 8. Performance Considerations

- Uses asynchronous requests to improve crawling speed
- Implements politeness delays to avoid overloading target servers
- Utilizes caching to prevent redundant crawling of previously visited pages

## 9. Error Handling

- Logs all errors and exceptions
- Provides detailed error messages in the output
- Implements retry mechanism for failed requests

## 10. Security Considerations

- Sanitizes all user inputs to prevent injection attacks
- Implements rate limiting to prevent abuse
- Respects robots.txt and user-specified crawling rules

## 11. Extensibility

The system is designed to be easily extensible:
- Modular architecture allows for easy addition of new features
- Plugin system for custom data extractors and output generators

## 12. Testing

- Unit tests for all major components
- Integration tests for end-to-end crawling scenarios
- Performance benchmarks for crawling speed and resource usage