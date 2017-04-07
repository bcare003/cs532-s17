import json

def Males():
    f = open('males', 'w')
    userDataFile = open("userData2.json","r")
    userData = json.load(userDataFile)
    count = 0
    countM = 0
    for user in userData:
        count += 1
        if user['user_details']['gender'] =='M':
            countM += 1
            f.write(json.dumps(user) + ',\n')


def Males22():
    f = open('males', 'r')
    userData = json.load(f)
    f1 = open('males22', 'w')
    count24 = 0
    countM = 0
    for user in userData:
        countM += 1
        if user['user_details']['age'] == '22':
            count24 += 1
            f1.write(json.dumps(user) + ',\n')


def Males22Student():
    f = open('males22', 'r')
    userData = json.load(f)
    f1 = open('males22Student', 'w')
    count22 = 0
    countStudent = 0
    for user in userData:
        count22 += 1
        if user['user_details']['occupation'] == 'student':
            countStudent += 1
            f1.write(json.dumps(user) + ',\n')


def HighLowRatings():
    f = open('3matches.json', 'r')
    f1 = open('3matchesPlus.json', 'w')
    userData = json.load(f)
    dict= {}
    for user in userData:
        dict['user_id'] = user['user_id']
        for movie in user['movie_details']:
            if movie['movie_rating'] == '5' or movie['movie_rating'] == '4':
                dict['type'] = 'Top Rated'
                dict['movie_id'] = movie['movie_id']
                dict['movie_name'] = movie['movie_name']
                dict['movie_rating'] = movie['movie_rating']
                f1.write(json.dumps(dict) + ',\n')
            if movie['movie_rating'] == '1':
                dict['type'] = 'Least Rated'
                dict['movie_id'] = movie['movie_id']
                dict['movie_name'] = movie['movie_name']
                dict['movie_rating'] = movie['movie_rating']
                f1.write(json.dumps(dict) + ',\n')

#Males()
#Males22()
#Males22Student()
HighLowRatings()
