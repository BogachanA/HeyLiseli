# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_liseli_lise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liseli',
            name='lise',
            field=models.CharField(choices=[('1', 'Robert Kolej'), ('2', 'Üsküdar Amerikan Lisesi'), ('3', 'İstanbul Erkek Lisesi'), ('4', 'Galatasaray Lisesi'), ('5', 'Doğa Koleji')], default='Gittiğin Lise', max_length=150),
        ),
    ]
