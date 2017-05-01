import feedparser
import re
rss_url = "http://top10000s.blogspot.com/feeds/posts/default?max-results=110"

feed = feedparser.parse(rss_url)

for post in feed.entries:
    titles = post.title
    pTitles = re.sub('[0-9].','',titles)
    pTitles2 = re.sub('\.', '', pTitles)
    print pTitles2