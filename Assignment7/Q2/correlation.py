import json
import re
from math import sqrt

#code taken directly from the PCI text, found at https://github.com/arthur-e/Programming-Collective-Intelligence/blob/master/chapter2/recommendations.py
def sim_pearson(prefs, p1, p2):
    '''
    Returns the Pearson correlation coefficient for p1 and p2.
    '''

    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # If they are no ratings in common, return 0
    if len(si) == 0:
        return 0
    # Sum calculations
    n = len(si)
    # Sums of all the preferences
    sum1 = 0
    for it in si:
        sum1 = sum1 + int(prefs[p1][it])
    #repeated above code
    sum2 = 0
    for it in si:
        sum2 = sum2 + int(prefs[p2][it])
    # Sums of the squares
    sum1Sq = 0
    for it in si:
        sum1Sq = sum1Sq + pow(int(prefs[p1][it]), 2)
    sum2Sq = 0
    for it in si:
        sum2Sq = sum2Sq + pow(int(prefs[p2][it]), 2)
    # Sum of the products
    pSum = 0
    for it in si:
        pSum = pSum + (int(prefs[p2][it]) * int(prefs[p1][it]))
    # Calculate r (Pearson score)
    num = pSum - ((sum1 * sum2) / 2)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r


def findCorrelation():
    userDataFile = open("userData2.json","r")
    userData = json.load(userDataFile)

    correlation_dic = {}
    for user in userData:
        user_id = user['user_id']
        movie_details_dic = {}
        for movie in user['movie_details']:
            movie_id = movie['movie_id']
            movie_rating = movie['movie_rating']
            movie_details_dic[movie_id] = movie_rating

        correlation_dic[user_id] = movie_details_dic
    return correlation_dic

correlation_dic = findCorrelation()
user_min = []
user_max = []
max = [-10, -10, -10, -10, -10]
min = [10, 10, 10, 10, 10]

#compare substitute me, user 459 to the other users in the data set
for user in correlation_dic:
    if(user != '459'):
        result = sim_pearson(correlation_dic, '459', user)
        if(max[0] < result):
            max[0] = result
            max.sort()
            user_max.append(user)
        if(min[0] > result):
            min[0] = result
            min.sort()
            min.reverse()
            user_min.append(user)

print max
print '\n'
print user_max[-5:]
print '\n'
print min
print '\n'
print user_min[-5:]