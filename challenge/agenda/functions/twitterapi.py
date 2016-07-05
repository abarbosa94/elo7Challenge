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

    def get_user_status(self, screen_names, contact):
        user_status = ''
        for screen_name in screen_names:
            if screen_name == contact.twitter_user:
                user_status =  api.user_timeline(screen_name = screen_name, count = 1)
                break;
            else:
                pass
        return user_status

    def get_last_tweet(self, screen_names, contacts):
        i = 0
        for contact in contacts:
            user_status = self.get_user_status(screen_names,contact)
            print len(user_status)
            contact = Contact.objects.filter(id=contact.id)[0]
            if len(user_status) != 0 :
                tweet_unique = user_status[0]
                if len(contact.twitter_user) != 0:
                    contact.last_tweet = tweet_unique.text
                    contact.save()
                else:
                    contact.last_tweet = contact.name+' nao informou uma conta do twitter ):'
                    contact.save()
            else:
                contact.last_tweet = contact.name+' ainda nao publicou nenhum tweet !'
                contact.save()
        return contacts