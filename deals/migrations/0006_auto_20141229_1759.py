# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='votes',
            field=models.ManyToManyField(blank=True, to='deals.Deal'),
        ),
    ]
