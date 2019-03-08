# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-07 16:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PostBar', '0008_userprofile_followings'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='liked_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]