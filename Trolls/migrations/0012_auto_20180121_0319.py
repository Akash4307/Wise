# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-21 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trolls', '0011_auto_20180118_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='UserLocation',
            field=models.CharField(default='null', max_length=500),
        ),
    ]
