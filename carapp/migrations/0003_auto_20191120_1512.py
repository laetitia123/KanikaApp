# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-11-20 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0002_auto_20191120_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spareparts',
            old_name='Phones',
            new_name='Phone',
        ),
    ]