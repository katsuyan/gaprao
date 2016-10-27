# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugyo', '0016_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='year',
            name='jugyo',
        ),
        migrations.AddField(
            model_name='year',
            name='jugyo',
            field=models.ManyToManyField(related_name='year', to='jugyo.Jugyo', verbose_name='授業'),
        ),
    ]