# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 17:42
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(choices=[('ABANILLA', (('Dionisio Bueno', 'Dionisio Bueno'), ('Sant\xedsima Cruz', 'Sant\xedsima Cruz'))), ('\xc1GUILAS', (('Juan XXIII', 'Juan XXIII'), ('La Caracola', 'La Caracola')))], max_length=100)),
                ('report_name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('level', models.CharField(max_length=150)),
                ('name', models.CharField(blank='True', default='', max_length=30)),
                ('surname', models.CharField(blank='True', default='', max_length=60)),
                ('email', models.EmailField(blank='True', default='', max_length=254)),
                ('phone_number', models.CharField(blank='True', default='', max_length=9, validators=[django.core.validators.RegexValidator(message='El n\xfamero de tel\xe9fono debe tenerel siguiente formato: 000000000. Hasta 9 d\xedgitos permitidos.', regex='^\\?1?\\d{9}$')])),
            ],
        ),
    ]