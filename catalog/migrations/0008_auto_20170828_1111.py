# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_internship_view_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='liseli',
            name='grade',
            field=models.CharField(choices=[('Prep', 'Hazırlık'), ('9', '9. sınıf'), ('10', '10. sınıf'), ('11', '11. sınıf'), ('12', '12. sınıf'), ('Done', 'Liseyi Bitirdim')], default='Hazırlık', max_length=100),
        ),
        migrations.AlterField(
            model_name='provider',
            name='facebook',
            field=models.URLField(default='none.com', max_length=400),
        ),
        migrations.AlterField(
            model_name='provider',
            name='hq_adress',
            field=models.CharField(default='none.com', max_length=400),
        ),
        migrations.AlterField(
            model_name='provider',
            name='linkedin',
            field=models.URLField(default='none.com', max_length=400),
        ),
        migrations.AlterField(
            model_name='provider',
            name='twitter',
            field=models.URLField(default='none.com', max_length=400),
        ),
    ]