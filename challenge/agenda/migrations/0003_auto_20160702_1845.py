# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20160702_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(unique=True, max_length=320, error_messages={b'unique': b'Ja existe um usuario com este email'}),
        ),
    ]
