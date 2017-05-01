import feedparser
import re
import sys

numEntries=0
reload(sys)
sys.setdefaultencoding('utf-8')


data = feedparser.parse('http://top10000s.blogspot.com/feeds/posts/default?max-results=110')
summaries = []
titles = []

outFile1 = open ('dataTitles.txt','wb')
outFile2 = open('dataContent.txt','wb')
outFile3 = open('dataCombined.txt','wb')

def parsing(summary,title):
   global numEntries
   print '\n'
   numEntries = numEntries + 1

   print numEntries
   print title
   print summary
   print '\n'

   substitute_1= re.sub('<[^>]*>',' ', summary)
   substitute_2= re.sub('   Continue reading...','',substitute_1)
   substitute_3= re.sub('  ',' ',substitute_2)

   #modified from grabContent.py
   omit_1 = title+" "+substitute_3
   omit_2 = re.sub("'","\\\\'",omit_1)
   omit_3 = re.sub('"','',omit_2)
   omit_4 = re.sub("`",'',omit_3)
   omit_5 = re.sub("[0-9]+\.", '', omit_4)
   print omit_5
   return title,substitute_3,omit_5
   print '\n'

#taken from class  PowerPoint
for e in data.entries:

   if 'summary' in e:
       summary = e.summary
   else:
       summary = e.description


   parsedtitle, parsedsummary, combinedsumtitle = parsing(summary,e.title)

   outFile1.write(parsedtitle)
   outFile1.write('\n')

   outFile2.write(parsedsummary)
   outFile2.write('\n')

   outFile3.write(combinedsumtitle)
   outFile3.write('\n')


