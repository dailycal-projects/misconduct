# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 00:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misconduct', '0005_auto_20160924_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='position',
            new_name='respondent_position',
        ),
    ]
