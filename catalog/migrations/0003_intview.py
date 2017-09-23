# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 12:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20170813_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime(2017, 8, 26, 12, 15, 20, 104612))),
                ('ip', models.CharField(max_length=40)),
                ('session_key', models.CharField(max_length=40)),
                ('rel_int', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='InternshipViews', to='catalog.Internship')),
            ],
        ),
    ]