# main.py

from tmv_scraper import get_torrent_data

def main():
    # உங்கள் torrent விவரக்கை url இட்டுக்கோங்க
    url = "https://example.com/torrent-page"

    # Torrent data process
    get_torrent_data(url)

    # Memory clear (avoid R14 error in Heroku)
    try:
        del url
    except:
        pass

if __name__ == "__main__":
    main()
