# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-14 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20170608_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
