# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-06 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostBar', '0006_auto_20190303_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='background',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(default='', max_length=128),
        ),
    ]
