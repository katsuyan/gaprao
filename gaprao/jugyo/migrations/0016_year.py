# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 03:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jugyo', '0015_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('year', models.IntegerField(verbose_name='年度')),
                ('jugyo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='year', to='jugyo.Jugyo', verbose_name='授業')),
            ],
        ),
    ]