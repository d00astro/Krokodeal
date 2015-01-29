# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0007_auto_20150102_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='imageUrl_url',
            field=models.URLField(default='http://lorempixel.com/g/100/100/cats'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='vendor_text',
            field=models.CharField(max_length=100, blank=True, null=True),
        ),
    ]
