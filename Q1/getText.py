import urllib2
import hashlib
from hashlib import md5
import os

fh = open("URIfinal.txt", 'r')

for line in fh:
    url = line
    url = url.replace('\n', '')

    def computeMD5(message):
        m = hashlib.md5()
        m.update(message)
        return m.hexdigest()

    hashMessage = computeMD5(url)
    print hashMessage

    # % lynx -dump -force_html www.cnn.com > www.cnn.com.processed example from assignment prompt
    os.system("lynx -dump -force_html " + url + "  > /bcarey/PROCESSED" + hashMessage + ".txt ")

