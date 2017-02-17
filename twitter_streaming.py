#Import the necessary methods from tweepy library
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "824820399762452480-9FZmzAd7MfHiBHgW5GMRBeel1qbVjZg"
access_token_secret = "cT7rQHs4ytUZ6E9OqKfGYvJGpHkxIwcbIhAaRtmqo86e2"
consumer_key = "D3MfZP8WxfogxUxJ1dVAHXaZn"
consumer_secret = "QsIB7CUyrFVONuqUjEE5nIhBvUHrsz5HYC5H2nw9kmUEnAK45o"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        tweet = json.loads(data)
        for url in tweet["entities"]["urls"]:
            print " %s" % url["expanded_url"]
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keyword: '#NFL'
    stream.filter(track=[ '#NFL', 'WWE', '#WWE', 'Bray Wyatt', 'John Cena', 'Roman Reigns'])