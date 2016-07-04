# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import agenda.models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_auto_20160702_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='last_tweet',
            field=models.CharField(max_length=140, blank=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='twitter_user',
            field=models.CharField(blank=True, max_length=120, validators=[agenda.models.validate_screen_name]),
        ),
    ]
