# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misconduct', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='description',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='case',
            name='position',
            field=models.CharField(default=' ', max_length=256),
            preserve_default=False,
        ),
    ]
