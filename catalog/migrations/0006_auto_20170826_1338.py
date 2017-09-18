# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-26 13:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
        ('catalog', '0005_auto_20170826_1223'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiseliSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessions.Session')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='intview',
            old_name='session_key',
            new_name='session_key_or_user_id',
        ),
    ]
