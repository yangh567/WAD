# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-07 17:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostBar', '0010_auto_20190307_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='question',
            name='viewed_users',
            field=models.ManyToManyField(related_name='viewed_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
