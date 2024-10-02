# WebAtlas: Comprehensive Web Crawler and Analyzer

## Overview

WebAtlas is a versatile and powerful web crawler designed to systematically browse and analyze websites. It extracts key information, generates structured output, and provides interactive visualizations of website structures. This tool is ideal for SEO analysis, content auditing, and website structure exploration.

## Features

- Configurable crawling parameters (depth, delay, user agent, etc.)
- Subdomain crawling support
- Exclude patterns for focused crawling
- Unique URL handling to prevent duplicate crawling
- Hierarchical tree structure generation of crawled pages
- Interactive graph visualization of site structure
- Detailed progress reporting during crawling
- Data extraction including title, meta description, links, and content
- JSON output for each crawled page
- Broken link detection and reporting
- Web-based configuration interface

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/charlpcronje/webatlas.git
   cd webatlas
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Ensure you have PHP installed on your server (for the web interface).

## Usage

### Web Interface

1. Place the `crawler_config.html` and `start_crawler.php` files in your web server's document root.
2. Access the configuration page through your web browser.
3. Fill out the crawl configuration and submit the form.
4. Monitor the crawl progress in real-time.
5. Once complete, access the interactive dashboard to explore the results.

### Command Line

You can also run WebAtlas from the command line:

```
python -m webatlas --config path/to/config.json
```

## Configuration

WebAtlas uses a JSON configuration file with the following key settings:

- `start_url`: The initial URL to start crawling
- `max_depth`: Maximum depth of crawling
- `delay`: Time to wait between requests
- `crawl_subdomains`: Whether to crawl subdomains
- `output_dir`: Directory to save output files
- `exclude_patterns`: List of URL patterns to exclude
- Other settings for user agent, timeout, max retries, etc.

For a full list of configuration options, see the `spec.md` file.

## Output

WebAtlas generates several output files:

- JSON files for each crawled page
- A tree structure of the crawled website
- An interactive graph visualization
- A list of broken links
- HTML content of pages (if enabled)

## Dashboard

The dashboard provides an interactive way to explore the crawl results:

- View the site structure as a graph
- Explore individual page data
- Analyze broken links
- View overall crawl statistics

## Supporting Documents
This app is not done yet, here are the remaining tasks:
- [Full Spec](./docs/spec.md)
- [Progress](./docs/progress.md)
- [Todo](./docs/todo.md)