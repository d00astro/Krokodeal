# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0008_auto_20150127_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='slug',
            field=models.SlugField(blank=True, default=datetime.date(2015, 2, 12), max_length=60),
            preserve_default=False,
        ),
    ]
