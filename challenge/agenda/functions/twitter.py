import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'A74fus0vAo1j6unNN6hWbnPVU'
consumer_secret = 'b00EM2FxYk7Kym80daQ9l54I1myp4oys8r50Dph0Xn1TLGv4pK'
access_token = '253814043-XQEXI7YVWYbSXYMzAhVRbAIN2z4hVD3ToWLavCuK'
access_secret = '9S54Lp0J6ptSyuJt93D75qAjcL78PTLBTKmDC8hKlpUMZ'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


class Test():
    def get_last_tweet(self, screen_name):
        tweet = api.user_timeline(screen_name = screen_name, count = 1)[0]
        return tweet.text