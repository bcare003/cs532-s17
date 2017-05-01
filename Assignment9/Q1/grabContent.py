import feedparser
import re

rss_url = "http://top10000s.blogspot.com/feeds/posts/default?max-results=110"

feed = feedparser.parse(rss_url)

contents = []
count = 0
for entry in feed.entries:
   if 'content' in entry:
       content = entry.content

   contents.append(entry.content)

subList = contents[:100]

for content in subList:
   count += 1
   print '\n'

   parse1 = re.sub('<[^>]*>', ' ', str(content))
   parse2 = parse1[126:]
   parse3 = re.sub("\\\\",'', parse2)
   parse4 = re.sub("   ",' ', parse3)
   parse5 = re.sub("  ", ' ', parse4)
   parse6 = re.sub("nbsp",'', parse4)

   print '\n'
   print parse5
