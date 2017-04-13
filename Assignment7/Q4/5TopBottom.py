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

def topMatches(
    prefs,
    person,
    n=5,
    similarity=sim_pearson, Flag1 = True
):
    '''
    Returns the best matches for person from the prefs dictionary.
    Number of results and similarity function are optional params.
    '''

    scores = [(similarity(prefs, person, other), other) for other in prefs
              if other != person]
    scores.sort()


    if (Flag1):
        scores.reverse()
    upperLimit = len(scores)
    lowerLimit = upperLimit - 5
    upperScores = scores[0:5]
    lowerScores = scores[lowerLimit:upperLimit]
    scoreResult = []
    for item in upperScores:
        scoreResult.append(item)
    for item in lowerScores:
        scoreResult.append(item)

    return scoreResult

def transformPrefs(prefs):
    '''
    Transform the recommendations into a mapping where persons are described
    with interest scores for a given title e.g. {title: person} instead of
    {person: title}.
    '''

    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            # Flip item and person
            result[item][person] = prefs[person][item]
    return result

def calculateSimilarItems(prefs, movieName, simMeasure, n=10, Flag1=True, Flag2=True):
    '''
    Create a dictionary of items showing which other items they are
    most similar to.
    '''

    result = {}
    # Invert the preference matrix to be item-centric
    if (Flag2):
        itemPrefs = transformPrefs(prefs)
    else:
        itemPrefs = prefs

    for item in itemPrefs:

        scores = topMatches(itemPrefs, item, n=n, similarity=simMeasure, Flag1=Flag1)
        result[item] = scores
        if item.lower() in movieName.lower():
            return result
    return result

def loadMovieLens(path='./movieData'):
    movies={}
    for line in open(path+'/u.item'):
        (id,title)=line.split('|')[0:2]
        movies[id]=title
    prefs={}
    for line in open(path+'/u.data'):
        (user,movieid,rating,ts)=line.split('\t')
        prefs.setdefault(user,{})
        prefs[user][movies[movieid]]=float(rating)
    return prefs, movies

movieLensRating, moviesData = loadMovieLens()
#654(Chinatown) & 1184(The Endless Summer 2)
filmTitle = moviesData['1184']
result1 = calculateSimilarItems(movieLensRating, filmTitle,simMeasure=sim_pearson, n=10, Flag1=True, Flag2=True)
item = result1[filmTitle]

print 'Top 5 & Bottom 5 Movies: ', filmTitle
for film in item[0:5]:
    print film
for film in item[5:10]:
    print film

