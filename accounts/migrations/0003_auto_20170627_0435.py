# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]