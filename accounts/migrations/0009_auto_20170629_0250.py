# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20170628_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last',
            field=models.CharField(default='', max_length=10),
        ),
    ]
