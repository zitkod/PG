import sys
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
import requests


class LinkParser(HTMLParser):
    def __init__(self, base_url):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.found = []
        self._seen = set()

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "a":
            return
        for name, value in attrs:
            if name.lower() == "href" and value:
                href = value.strip()
                lower = href.lower()
                if lower.startswith(("mailto:", "javascript:", "tel:", "data:")):
                    return
                abs_url = urljoin(self.base_url, href)
                p = urlparse(abs_url)
                abs_url_no_fragment = p._replace(fragment="").geturl()
                if abs_url_no_fragment not in self._seen:
                    self._seen.add(abs_url_no_fragment)
                    self.found.append(abs_url_no_fragment)


def download_url_and_get_all_hrefs(url):
    try:
        response = requests.get(url, timeout=15)
    except requests.RequestException as e:
        raise RuntimeError(f"Chyba při stahování URL: {e}") from e

    if response.status_code != 200:
        raise RuntimeError(f"HTTP status code není 200 (je {response.status_code})")

    html = response.text

    parser = LinkParser(base_url=response.url)
    parser.feed(html)
    return parser.found


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Použití: python sixth.py <url>")
            sys.exit(1)
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        for h in hrefs:
            print(h)
    except Exception as e:
        print(f"Program skončil chybou: {e}")
        sys.exit(2)
