# -*- coding: utf-8 -*-
from django import forms
from models import Contact

class ContactForm(forms.ModelForm):

        class Meta:
                model = Contact
                fields = ('name', 'email', 'twitter_user')