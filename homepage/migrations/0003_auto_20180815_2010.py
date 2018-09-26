# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-15 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20180815_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assignment',
            field=models.FileField(upload_to=homepage.models.upload_location),
        ),
        migrations.AlterField(
            model_name='subjects_teaching',
            name='assignment_given',
            field=models.FileField(upload_to=homepage.models.upload_location, verbose_name='Assignment'),
        ),
        migrations.AlterField(
            model_name='subjects_teaching',
            name='solution',
            field=models.FileField(upload_to=homepage.models.upload_location, verbose_name='Solution'),
        ),
    ]