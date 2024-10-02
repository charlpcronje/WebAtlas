# webatlas/core/data_extractor.py

from bs4 import BeautifulSoup
from urllib.parse import urljoin

class DataExtractor:
    def extract(self, response, base_url):
        soup = BeautifulSoup(response.content, 'html.parser')
        return {
            "url": response.url,
            "title": soup.title.string if soup.title else "",
            "meta_description": self._get_meta_description(soup),
            "links": self._get_unique_full_links(soup, base_url),
            "h1": self._get_h1(soup),
            "content": self._get_main_content(soup),
        }

    def _get_meta_description(self, soup):
        meta = soup.find("meta", attrs={"name": "description"})
        return meta["content"] if meta else ""

    def _get_unique_full_links(self, soup, base_url):
        links = set()
        for a in soup.find_all("a", href=True):
            full_url = urljoin(base_url, a['href'])
            links.add(full_url)
        return list(links)

    def _get_h1(self, soup):
        h1 = soup.find("h1")
        return h1.text.strip() if h1 else ""

    def _get_main_content(self, soup):
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        # Get text
        text = soup.get_text()
        # Break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # Break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # Drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        return text