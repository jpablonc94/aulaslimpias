# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='centro',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.TextField(default='', max_length=9),
        ),
        migrations.AlterField(
            model_name='profile',
            name='responsable',
            field=models.TextField(default='', max_length=100),
        ),
    ]
