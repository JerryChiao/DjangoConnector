# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_example', '0002_auto_20171218_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.AlterField(
            model_name='category',
            name='content',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='\u63cf\u8ff0'),
        ),
    ]