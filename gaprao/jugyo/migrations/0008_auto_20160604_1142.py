# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 02:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jugyo', '0007_remove_jugyo_year'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NoJugyoDay',
            new_name='NoJugyo',
        ),
    ]
