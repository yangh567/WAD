# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-15 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostBar', '0015_question_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='answer_images'),
        ),
    ]