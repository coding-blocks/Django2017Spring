# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-09 11:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_01.MyUser'),
        ),
    ]
