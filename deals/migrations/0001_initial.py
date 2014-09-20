# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title_text', models.CharField(max_length=200)),
                ('link_url', models.URLField()),
                ('vendor_text', models.CharField(max_length=100)),
                ('price_decimal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('description_text', models.TextField()),
                ('imageUrl_url', models.URLField()),
                ('normalPrice_decimal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('shippingCost_decimal', models.DecimalField(max_digits=10, decimal_places=2)),
                ('discountCode_text', models.CharField(max_length=200)),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
                ('expired', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
