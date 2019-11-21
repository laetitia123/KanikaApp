# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-21 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0004_merge_20191121_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='sparePart',
            field=models.ManyToManyField(blank=True, null=True, to='carapp.SpareParts'),
        ),
        migrations.AlterField(
            model_name='spareparts',
            name='categoryImage',
            field=models.ImageField(upload_to='category/'),
        ),
        migrations.AlterField(
            model_name='spareparts',
            name='categoryPart',
            field=models.CharField(choices=[('Toyota', 'Toyota'), ('Cross country', 'Cross country'), ('Vox wagen', 'Vox wagen'), ('Suzuki', 'Suzuki'), ('Mahindra', 'Mahindra'), ('Honda', 'Honda'), ('Hyunda', 'Hyunda'), ('Volvo', 'Volvo'), ('Daihatsu', 'Daihatsu')], max_length=40),
        ),
        migrations.AlterField(
            model_name='spareparts',
            name='namePart',
            field=models.CharField(choices=[('Head lights', 'Head lights'), ('Brake lights', 'Brake lights'), ('Tail lights', 'Tail lights'), ('Tail gate', 'Tail gate'), ('Mirrors', 'Mirrors'), ('Hoods', 'Hoods'), ('Window', 'Window'), ('Door', 'Door'), ('Tyres', 'Tyres'), ('Petrol tank', 'Petrol tank'), ('Roof', 'Roof'), ('Steering wheel', 'Steering wheel'), ('radiator', 'radiator')], max_length=40),
        ),
    ]
