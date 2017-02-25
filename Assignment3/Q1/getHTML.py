import urllib2
import hashlib
from hashlib import md5
import os

input = open("URIfinal.txt", 'r')

for line in input:
    url = line
    url = url.replace('\n', '')

    # referenced from http://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python
    def convert_to_md5(content):
        m = hashlib.md5()
        m.update(content)
        return m.hexdigest()

    output = convert_to_md5(url)
    print output

    # % wget - O www.cnn.com http: // www.cnn.com / provided on assignment prompt
    os.system(" wget -O /bcarey/HTML" + output + ".txt " + url)
