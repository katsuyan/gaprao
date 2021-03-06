# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugyo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='授業名')),
                ('room', models.CharField(max_length=255, verbose_name='教室')),
                ('syllabus_url', models.CharField(max_length=255, verbose_name='シラバスURL')),
                ('year', models.CharField(max_length=255, verbose_name='年度')),
                ('term', models.CharField(max_length=255, verbose_name='学期')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
