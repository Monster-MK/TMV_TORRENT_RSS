# main.py

from tmv_scraper import get_torrent_data

def main():
    # உங்கள் torrent விவரக்கை url இட்டுக்கோங்க
    url = "https://example.com/torrent-page"
    get_torrent_data(url)

if __name__ == "__main__":
    main()
