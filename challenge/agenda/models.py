from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import tweepy
from tweepy import OAuthHandler


def validate_name(value):
    name = str(value)
    name = name.split();
    if len(name) == 1:
        raise ValidationError(
            _('O nome precisa ter, no minimo, duas palavras')
        )
    for word in name:
        if len(word)<2:
            raise ValidationError(
            _('Cada palavra que compoe o nome deve ter ao menos duas letras')
            )

def validate_screen_name(value):
        #it was necessary to repeat auth code here because twitterapi module uses this module and this module would use twitterapi module
        consumer_key = 'A74fus0vAo1j6unNN6hWbnPVU'
        consumer_secret = 'b00EM2FxYk7Kym80daQ9l54I1myp4oys8r50Dph0Xn1TLGv4pK'
        access_token = '253814043-XQEXI7YVWYbSXYMzAhVRbAIN2z4hVD3ToWLavCuK'
        access_secret = '9S54Lp0J6ptSyuJt93D75qAjcL78PTLBTKmDC8hKlpUMZ'
         
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
         
        api = tweepy.API(auth)
        try:
            api.get_user(value)
        except tweepy.TweepError:
            raise ValidationError(
                _('Por favor, informe um usuario que exista')
            )

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=42,validators=[validate_name])
    email = models.EmailField(max_length = 320, unique=True,  error_messages={'unique':"Ja existe um usuario com este email"})
    twitter_user = models.CharField(max_length = 120, blank=True, validators=[validate_screen_name])
    last_tweet = models.CharField(max_length = 140, blank = True)

    def __unicode__(self):
        return self.name

