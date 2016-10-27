# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 02:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jugyo', '0005_homework'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='テスト名')),
                ('day', models.DateField(verbose_name='テスト日')),
                ('exam_info', models.TextField(verbose_name='テスト範囲')),
                ('jugyo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_day', to='jugyo.Jugyo', verbose_name='授業')),
            ],
        ),
        migrations.RemoveField(
            model_name='testday',
            name='jugyo',
        ),
        migrations.DeleteModel(
            name='TestDay',
        ),
    ]
