# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-07 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misconduct', '0002_auto_20170307_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='clarification',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
