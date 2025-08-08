import feedparser

def fetch_rss(url):
    # RSS feed parse
    feed = feedparser.parse(url)

    # 10 items மட்டும் எடுக்க
    entries = feed.entries[:10]

    # பெரிய feed object memory release
    try:
        del feed
    except:
        pass

    return entries
