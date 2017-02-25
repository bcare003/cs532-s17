import urllib2
import hashlib
from hashlib import md5
import os
# copied from getHTML.py
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

    # % lynx -dump -force_html www.cnn.com > www.cnn.com.processed example from assignment prompt
    os.system("lynx -dump -force_html " + url + "  > /bcarey/PROCESSED" + hashMessage + ".txt ")

