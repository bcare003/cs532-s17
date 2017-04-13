import clusters

blognames, words, data = clusters.readfile('blogdata1.txt')

c = clusters.scaledown(data)

clusters.draw2d(c, blognames, jpeg='mds.jpg')