# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 03:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jugyo', '0012_auto_20160604_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='jugyo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_day', to='jugyo.Jugyo', verbose_name='授業'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='jugyo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homework', to='jugyo.Jugyo', verbose_name='授業'),
        ),
        migrations.AlterField(
            model_name='nojugyo',
            name='jugyo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='no_jugyo', to='jugyo.Jugyo', verbose_name='授業'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='jugyos',
            field=models.ManyToManyField(related_name='teachers', to='jugyo.Jugyo', verbose_name='授業'),
        ),
        migrations.AlterField(
            model_name='upjugyo',
            name='jugyo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='up_jugyo', to='jugyo.Jugyo', verbose_name='授業'),
        ),
    ]
