# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-23 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page_example', '0007_vnacombocable'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrequencyPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.FloatField()),
                ('comments', models.CharField(max_length=100)),
                ('reserved1', models.CharField(max_length=100)),
                ('reserved2', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FrequencyStandingWave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standing_wave', models.FloatField()),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('category_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_example.Category')),
                ('frequency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_example.FrequencyPoint')),
                ('polar_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_example.Polar')),
            ],
        ),
    ]
