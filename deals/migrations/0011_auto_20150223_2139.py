# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0010_deal_thumbnail_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='thumbnail_image_height',
            field=models.PositiveIntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='thumbnail_image_width',
            field=models.PositiveIntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deal',
            name='thumbnail_image',
            field=models.ImageField(blank=True, upload_to='', null=True, height_field='thumbnail_image_height', width_field='thumbnail_image_width'),
        ),
    ]
