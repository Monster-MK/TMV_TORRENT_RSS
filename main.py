from tmv_scraper import fetch_rss

def main():
    # உங்க RSS feed URL இங்கே போடு
    url = "https://example.com/rss-feed"

    # RSS data fetch
    entries = fetch_rss(url)

    # Data print or process
    for item in entries:
        print(f"Title: {item.title}")
        print(f"Link: {item.link}")
        print("-" * 40)

    # Memory release
    try:
        del entries
    except:
        pass

if __name__ == "__main__":
    main()
