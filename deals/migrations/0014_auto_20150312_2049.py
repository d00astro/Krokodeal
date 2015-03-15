# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0013_auto_20150303_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='imageUrl_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
