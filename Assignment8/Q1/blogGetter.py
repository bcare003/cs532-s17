import requests
import generatefeedvector.py

def get100blogurls():
    f = open('100blogurls.txt', 'w')
    url_set = set()
    while (len(url_set) < 100):
        url = "http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117"
        generate_url = requests.get(url)
        final_url = generate_url.url.strip('?expref=next-blog/')
        url_set.add(final_url)
    for element in url_set:
        print element
        f.write(element + '\n')
    f.write('http://f-measure.blogspot.com' + '\n')
    f.write('http://ws-dl.blogspot.com')


def completeURL():
    input = open('100blogurls.txt', 'r')
    output = open('100completeurls.txt', 'w')
    for element in input:
        add = "/feeds/posts/default?alt=rss"
        item = element.strip() + add
        output.write(item + '\n')
        print item

#get100blogurls()
completeURL()

