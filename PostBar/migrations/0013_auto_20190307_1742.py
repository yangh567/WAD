# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-07 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostBar', '0012_answer_ranked_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='last_modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='last_modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]