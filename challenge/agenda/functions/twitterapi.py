import tweepy
from tweepy import OAuthHandler
from agenda.models import Contact
 
consumer_key = 'A74fus0vAo1j6unNN6hWbnPVU'
consumer_secret = 'b00EM2FxYk7Kym80daQ9l54I1myp4oys8r50Dph0Xn1TLGv4pK'
access_token = '253814043-XQEXI7YVWYbSXYMzAhVRbAIN2z4hVD3ToWLavCuK'
access_secret = '9S54Lp0J6ptSyuJt93D75qAjcL78PTLBTKmDC8hKlpUMZ'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


class Twitter():

    def get_last_tweet(self, screen_names, contacts):
        i = 0
        for i in range(0,len(screen_names)):
            user_status =  api.user_timeline(screen_name = screen_names[i], count = 1)
            contact = Contact.objects.filter(id=contacts[i].id)[0]
            if len(user_status) != 0 :
                tweet_unique = user_status[0]
                if len(screen_names[i]) != 0:
                    contact.last_tweet = tweet_unique.text
                    contact.save()
                else:
                    contact.last_tweet = contact.name+' nao informou uma conta do twitter ):'
                    contact.save()
            else:
                contact.last_tweet = contact.name+' ainda nao publicou nenhum tweet !'
                contact.save()
        return contacts