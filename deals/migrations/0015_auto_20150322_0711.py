# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0014_auto_20150312_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to='deal_thumbnails', height_field='thumbnail_image_height', width_field='thumbnail_image_width'),
        ),
    ]
