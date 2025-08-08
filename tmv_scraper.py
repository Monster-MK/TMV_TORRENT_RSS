import feedparser

def fetch_rss(url):
    feed = feedparser.parse(url)
    # RSS list-ஐ 10 items மட்டும் எடுக்க
    entries = feed.entries[:10]
    return entries
