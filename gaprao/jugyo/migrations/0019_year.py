# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugyo', '0018_auto_20160604_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField(verbose_name='年度')),
                ('jugyo', models.ManyToManyField(related_name='year', to='jugyo.Jugyo', verbose_name='授業')),
            ],
        ),
    ]
