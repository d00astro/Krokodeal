# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0011_auto_20150223_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='slug',
            field=models.SlugField(max_length=60, blank=True),
        ),
    ]
