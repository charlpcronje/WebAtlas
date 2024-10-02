webatlas/utils/output_generator.py

import os
import json
from urllib.parse import urlparse
import networkx as nx

class OutputGenerator:
    def __init__(self, config):
        self.output_dir = config.get("output_dir", "./output")
        self.save_html_flag = config.get("save_html", False)
        os.makedirs(self.output_dir, exist_ok=True)

    def save_data(self, data):
        filename = self._generate_filename(data["url"], "json")
        filepath = os.path.join(self.output_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def save_html(self, url, html_content):
        if self.save_html_flag:
            filename = self._generate_filename(url, "html")
            filepath = os.path.join(self.output_dir, "html", filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html_content)

    def save_tree_structure(self, tree_structure):
        filepath = os.path.join(self.output_dir, "tree_structure.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(tree_structure, f, ensure_ascii=False, indent=2)

    def save_graph(self, graph):
        graph_data = {
            "nodes": [{"id": node, "title": data.get('title', '')} for node, data in graph.nodes(data=True)],
            "links": [{"source": u, "target": v} for u, v in graph.edges()]
        }
        filepath = os.path.join(self.output_dir, "graph_data.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(graph_data, f, ensure_ascii=False, indent=2)

    def _generate_filename(self, url, extension):
        parsed_url = urlparse(url)
        path = parsed_url.path.strip("/").replace("/", "_")
        if not path:
            path = "index"
        return f"{parsed_url.netloc}_{path}.{extension}"