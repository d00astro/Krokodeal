# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0002_auto_20140920_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='normalPrice_decimal',
            field=models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='deal',
            name='shippingCost_decimal',
            field=models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2),
        ),
    ]
