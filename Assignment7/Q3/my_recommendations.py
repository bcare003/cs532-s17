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


def getRecommendations(prefs, person, similarity=sim_pearson):
    '''
    Gets recommendations for a person by using a weighted average
    of every other user's rankings
    '''

    totals = {}
    simSums = {}
    for other in prefs:
    # Don't compare me to myself
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        # Ignore scores of zero or lower
        if sim <= 0:
            continue
        for item in prefs[other]:
            # Only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                # The final score is calculated by multiplying each item by the
                #   similarity and adding these products together
                totals[item] += int(prefs[other][item]) * sim
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim
    # Create the normalized list
    rankings = [(total / simSums[item], item) for (item, total) in
                totals.items()]
    # Return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings


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


def getMovieName(id):
    moviesDataFile = open("movieData.json","r")
    movieData = json.load(moviesDataFile)
    for user in movieData:
        if user['movie_id'] == id:
            print user['movie_id']
            print user['movie_name']


correlation_dic = findCorrelation()
user_min = []
user_max = []
max = [-10, -10, -10, -10, -10]
min = [10, 10, 10, 10, 10]

#compare substitute me, user 459 to the other users in the data set
for user in correlation_dic:
    if (user != '501'):
        result = sim_pearson(correlation_dic, '501', user)
        if (max[0] < result):
            max[0] = result
            max.sort()
            user_max.append(user)
        if (min[0] > result):
            min[0] = result
            min.sort()
            min.reverse()
            user_min.append(user)

result = getRecommendations(correlation_dic, '501', similarity=sim_pearson)

Top_Movies = result[0:5]
Least_Movies = result[-5:]
print Top_Movies
print Least_Movies

for movie in Top_Movies:
    getMovieName(movie[1])

for movie in Least_Movies:
    getMovieName(movie[1])
