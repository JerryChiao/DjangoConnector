# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-27 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_example', '0011_auto_20171224_0951'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecentProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('property', models.TextField()),
                ('image', models.ImageField(upload_to=b'')),
                ('full_witc', models.CharField(max_length=30)),
                ('document', models.FileField(upload_to='vna_combo_cable/')),
                ('reserved1', models.CharField(max_length=100)),
                ('reserved2', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
