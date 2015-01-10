# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('deals', '0004_deal_temperature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('votes', models.ManyToManyField(to='deals.Deal')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
