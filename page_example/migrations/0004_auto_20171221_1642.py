# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-21 08:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page_example', '0003_converter_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upper_frequency', models.FloatField()),
                ('outer_diameter', models.FloatField()),
                ('resistance', models.FloatField()),
                ('loss_coef_k1', models.FloatField()),
                ('loss_coef_k2', models.FloatField()),
                ('image', models.ImageField(upload_to='cable/')),
                ('comments', models.CharField(max_length=100)),
                ('reserved1', models.CharField(max_length=100)),
                ('reserved2', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CableCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='cable',
            name='category_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_example.CableCategory'),
        ),
        migrations.AddField(
            model_name='cable',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page_example.Property'),
        ),
    ]