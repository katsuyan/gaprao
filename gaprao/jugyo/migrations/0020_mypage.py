# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 04:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jugyo', '0019_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('jugyo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jugyo.Jugyo', verbose_name='授業')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザ')),
            ],
        ),
    ]
