# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0009_deal_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='thumbnail_image',
            field=models.ImageField(upload_to='', blank=True, null=True),
            preserve_default=True,
        ),
    ]
