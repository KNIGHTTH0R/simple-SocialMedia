# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 16:49
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20170628_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=accounts.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
