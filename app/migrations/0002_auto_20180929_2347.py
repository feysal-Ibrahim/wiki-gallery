# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-29 20:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='category',
            new_name='image_category',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='location',
            new_name='image_location',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='location',
        ),
    ]
