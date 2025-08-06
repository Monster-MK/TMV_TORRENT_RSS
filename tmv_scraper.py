from scraper_utils import fetch_html, parse_html_with_bs4

def get_torrent_data(url):
    html = fetch_html(url)
    if html:
        title = parse_html_with_bs4(html)
        print(f"Page Title: {title}")
