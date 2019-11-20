# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-20 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0002_auto_20191120_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spareparts',
            name='namePart',
            field=models.CharField(choices=[(b'Head lights', b'Head lights'), (b'Brake lights', b'Brake lights'), (b'Tail lights', b'Tail lights'), (b'Tail gate', b'Tail gate'), (b'Mirrors', b'Mirrors'), (b'Hoods', b'Hoods'), (b'Window', b'Window'), (b'Door', b'Door'), (b'Tyres', b'Tyres'), (b'Petrol tank', b'Petrol tank'), (b'Roof', b'Roof'), (b'Steering wheel', b'Steering wheel'), (b'Engine', b'Engine')], max_length=40),
        ),
    ]
