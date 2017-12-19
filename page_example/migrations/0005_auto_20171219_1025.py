# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-19 02:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page_example', '0004_auto_20171218_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=30, verbose_name='\u63cf\u8ff0')),
                ('code', models.CharField(max_length=10, verbose_name='\u7f16\u53f7')),
            ],
        ),
        migrations.AlterField(
            model_name='connectorcable',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_example.Property'),
        ),
        migrations.AlterField(
            model_name='connectorpcb',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_example.Property'),
        ),
    ]
