import statistics
import math
import re

if __name__ == "__main__":

	with open('friend_num.txt') as input:
		followers = input.read()
	#https://docs.python.org/2/library/re.html
	followers = map(int, re.findall('\d+', followers))

	# https://pythonprogramming.net/statistics-python-3-module-mean-standard-deviation/
	print ' The mean number of friends is ' , statistics.mean(followers)

	print ' The median number of friends is ' , statistics.median(followers)

	print ' The standard deviation of the number of friends is ' , statistics.stdev(followers)

