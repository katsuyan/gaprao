# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugyo', '0013_auto_20160604_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='JugyoDateTime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.IntegerField(verbose_name='曜日')),
                ('period', models.IntegerField(verbose_name='時限')),
                ('jugyos', models.ManyToManyField(related_name='date_time', to='jugyo.Jugyo', verbose_name='授業')),
            ],
        ),
    ]