# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-27 14:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_example', '0013_auto_20180327_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentproduct',
            name='document',
            field=models.FileField(upload_to='recent/'),
        ),
        migrations.AlterField(
            model_name='recentproduct',
            name='image',
            field=models.ImageField(upload_to='recent/'),
        ),
    ]
