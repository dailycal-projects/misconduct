# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misconduct', '0002_auto_20160918_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='complaint_date',
            field=models.DateField(null=True),
        ),
    ]