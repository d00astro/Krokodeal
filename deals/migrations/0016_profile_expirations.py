# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0015_auto_20150322_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='expirations',
            field=models.ManyToManyField(to='deals.Deal', related_name='profilesThatExpired', blank=True),
            preserve_default=True,
        ),
    ]
