# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-08 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misconduct', '0005_case_include'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='include',
            field=models.BooleanField(default=False),
        ),
    ]
