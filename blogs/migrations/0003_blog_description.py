# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20170312_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
