# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_donejobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
