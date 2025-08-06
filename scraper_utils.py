# scraper_utils.py

import cloudscraper
from bs4 import BeautifulSoup
import gc

# ✅ One-time reusable scraper
scraper = cloudscraper.create_scraper()

def fetch_html(url):
    """
    Given a URL, return the HTML content using cloudscraper.
    """
    try:
        response = scraper.get(url, timeout=30)
        html = response.text
        response.close()  # ✅ Release connection
        return html
    except Exception as e:
        print(f"[scraper_utils] Error fetching {url}: {e}")
        return None

def parse_html_with_bs4(html):
    """
    Parse HTML content using BeautifulSoup.
    You can customize this to extract title, links, etc.
    """
    try:
        soup = BeautifulSoup(html, 'html.parser')
        
        # 🧪 Example: Get page title
        title = soup.title.string if soup.title else "No Title"

        # ✅ Cleanup
        soup.decompose()
        del soup
        gc.collect()

        return title
    except Exception as e:
        print(f"[scraper_utils] Error parsing HTML: {e}")
        return None
