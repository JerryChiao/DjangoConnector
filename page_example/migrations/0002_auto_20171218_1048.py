# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-18 10:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_example', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='code',
            field=models.CharField(max_length=10, verbose_name='\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='category',
            name='content',
            field=models.CharField(max_length=30, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='combinetype',
            name='code',
            field=models.CharField(max_length=10, verbose_name='\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='combinetype',
            name='content',
            field=models.CharField(max_length=30, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='installtype',
            name='code',
            field=models.CharField(max_length=10, verbose_name='\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='installtype',
            name='content',
            field=models.CharField(max_length=30, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='outlook',
            name='code',
            field=models.CharField(max_length=10, verbose_name='\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='outlook',
            name='content',
            field=models.CharField(max_length=30, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='polar',
            name='code',
            field=models.CharField(max_length=10, verbose_name='\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='polar',
            name='content',
            field=models.CharField(max_length=30, verbose_name='\u63cf\u8ff0'),
        ),
    ]