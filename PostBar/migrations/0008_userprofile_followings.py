# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-06 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostBar', '0007_auto_20190306_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='followings',
            field=models.ManyToManyField(related_name='followers', to='PostBar.UserProfile'),
        ),
    ]
