# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugyo', '0009_auto_20160604_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='名前')),
                ('jugyos', models.ManyToManyField(to='jugyo.Jugyo')),
            ],
        ),
    ]
