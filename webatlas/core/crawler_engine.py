webatlas/core/crawler_engine.py

import time
import requests
import re
import networkx as nx
from urllib.parse import urljoin, urlparse, urlunparse
from collections import deque
from webatlas.core.data_extractor import DataExtractor
from webatlas.utils.output_generator import OutputGenerator

class CrawlerEngine:
    def __init__(self, config_manager):
        self.config = config_manager
        self.data_extractor = DataExtractor()
        self.output_generator = OutputGenerator(self.config)
        self.unique_urls = set()
        self.tree_structure = {}
        self.total_links_found = 0
        self.total_links_scanned = 0
        self.exclude_patterns = [re.compile(pattern) for pattern in self.config.get("exclude_patterns", [])]
        self.max_depth = self.config.get("max_depth", 10)
        self.max_pages = self.config.get("max_pages", 100)
        self.graph = nx.DiGraph()

    def start(self):
        start_url = self.config.get("start_url")
        if not start_url:
            raise ValueError("Start URL is not specified in the configuration")
        print(f"Starting crawl from: {start_url}")
        print(f"Max depth: {self.max_depth}, Max pages: {self.max_pages}")
        self.crawl(start_url)
        print(f"\nCrawl completed.")
        print(f"Total unique pages found: {len(self.unique_urls)}")
        print(f"Total pages scanned: {self.total_links_scanned}")
        self.output_generator.save_graph(self.graph)

    def crawl(self, start_url):
        queue = deque([(start_url, 0)])
        while queue and len(self.unique_urls) < self.max_pages:
            url, depth = queue.popleft()
            if depth > self.max_depth:
                continue

            normalized_url = self.normalize_url(url)
            if normalized_url in self.unique_urls or self._is_excluded(normalized_url):
                continue

            self.unique_urls.add(normalized_url)
            self.add_to_tree_structure(normalized_url)
            self.total_links_scanned += 1

            print(f"\n[{self.total_links_scanned}/{self.max_pages}] Depth {depth}/{self.max_depth}: {normalized_url}")

            try:
                response = requests.get(
                    normalized_url, 
                    timeout=self.config.get("request_timeout", 30),
                    headers=self.config.get("headers", {}),
                    allow_redirects=self.config.get("follow_redirects", True)
                )
                response.raise_for_status()
            except requests.RequestException as e:
                print(f"  Error: {e}")
                continue

            extracted_data = self.data_extractor.extract(response, normalized_url)
            self.output_generator.save_data(extracted_data)
            self.output_generator.save_html(normalized_url, response.text)

            print(f"  Title: {extracted_data['title']}")
            print(f"  Links found: {len(extracted_data['links'])}")

            self.total_links_found += len(extracted_data['links'])

            # Add node and edges to the graph
            self.graph.add_node(normalized_url, title=extracted_data['title'])
            for link in extracted_data['links']:
                normalized_link = self.normalize_url(link)
                self.graph.add_edge(normalized_url, normalized_link)
                if self._should_crawl(link):
                    queue.append((link, depth + 1))

            delay = self.config.get("delay", 1)
            time.sleep(delay)

    def normalize_url(self, url):
        parsed = urlparse(url)
        normalized = urlunparse(parsed._replace(fragment=""))
        return normalized.rstrip('/') or normalized

    def _is_excluded(self, url):
        return any(pattern.search(url) for pattern in self.exclude_patterns)

    def add_to_tree_structure(self, url):
        parsed_url = urlparse(url)
        path_parts = parsed_url.path.strip('/').split('/')
        current_level = self.tree_structure

        for part in path_parts:
            if part:
                if part not in current_level:
                    current_level[part] = {}
                current_level = current_level[part]

        # Add the full URL as a leaf node
        current_level[url] = {}

    def _should_crawl(self, url):
        parsed_url = urlparse(url)
        start_url = urlparse(self.config.get("start_url"))
        crawl_subdomains = self.config.get("crawl_subdomains", False)

        if url in self.unique_urls or self._is_excluded(url):
            return False

        if crawl_subdomains:
            return parsed_url.netloc.endswith(start_url.netloc) or start_url.netloc.endswith(parsed_url.netloc)
        else:
            return parsed_url.netloc == start_url.netloc

    def get_tree_structure(self):
        return self.tree_structure