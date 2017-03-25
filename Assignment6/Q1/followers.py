#coding: utf-8
import tweepy
from tweepy import OAuthHandler
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def followMe():
    global api
#Variables that contains the user credentials to access Twitter API
access_token = "824820399762452480-9FZmzAd7MfHiBHgW5GMRBeel1qbVjZg"
access_token_secret = "cT7rQHs4ytUZ6E9OqKfGYvJGpHkxIwcbIhAaRtmqo86e2"
consumer_key = "D3MfZP8WxfogxUxJ1dVAHXaZn"
consumer_secret = "QsIB7CUyrFVONuqUjEE5nIhBvUHrsz5HYC5H2nw9kmUEnAK45o"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth, wait_on_rate_limit=True)

file = open('followerlist.txt', 'w+')

user = api.get_user("bryancarey432")

followers = []

for user in tweepy.Cursor(api.followers, count=50).items():
    followers.append((user.profile_image_url, user.screen_name, user.name, user.id_str))

    #print >> file, user.profile_image_url
    print >> file, user.screen_name
    #print >> file, user.name
    #print >> file, user.id_str

file.close()



