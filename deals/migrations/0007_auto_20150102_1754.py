# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0006_auto_20141229_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='votes',
        ),
        migrations.AddField(
            model_name='profile',
            name='downvotes',
            field=models.ManyToManyField(blank=True, related_name='profilesThatDownvoted', to='deals.Deal'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='profilesThatUpvoted', to='deals.Deal'),
            preserve_default=True,
        ),
    ]
