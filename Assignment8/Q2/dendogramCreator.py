import clusters
import sys

blognames, words, data = clusters.readfile('blogdata1.txt')

clust = clusters.hcluster(data)

clusters.printclust(clust, labels=blognames)
sys.stdout = open('ascii.text', 'w+')

clusters.drawdendrogram(clust, blognames, jpeg='dendogram.jpg')