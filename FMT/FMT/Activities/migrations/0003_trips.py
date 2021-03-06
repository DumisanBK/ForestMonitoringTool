# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activities', '0002_auto_20190311_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('trip_id', models.IntegerField()),
                ('date', models.DateField()),
                ('retailer', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=20)),
                ('item_spend', models.IntegerField()),
                ('item_units', models.IntegerField()),
            ],
        ),
    ]
