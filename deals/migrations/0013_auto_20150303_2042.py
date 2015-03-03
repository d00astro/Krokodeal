# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0012_auto_20150223_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='thumbnail_image_height',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='deal',
            name='thumbnail_image_width',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
