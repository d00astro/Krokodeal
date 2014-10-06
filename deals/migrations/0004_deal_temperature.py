# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0003_auto_20140921_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='temperature',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
