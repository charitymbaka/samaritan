# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 18:03
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tukiogram', '0004_auto_20170316_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tukio',
            name='location_geom',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, unique=True),
        ),
    ]