#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


CENTROS = (
    ('ABANILLA',(
        (u'Dionisio Bueno', u'Dionisio Bueno'),
        (u'Santísima Cruz', u'Santísima Cruz'),
        )
     ),
    ('ÁGUILAS', (
        (u'Juan XXIII', u'Juan XXIII'),
        (u'La Caracola', u'La Caracola'),
        )
     )
)

class Report(models.Model):

    school = models.CharField(max_length=100, choices=CENTROS)
    #report_name = models.CharField(max_length=150, blank='True', default='')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    level = models.CharField(max_length=150)
    name = models.TextField(blank='True', default='', max_length=30)
    email = models.EmailField(blank='True', default='')
    #phone_regex = RegexValidator(regex=r'^\?1?\d{9}$', message="El número de teléfono debe tener"
    #                                                          "el siguiente formato: 000000000. Hasta 9 dígitos permitidos.")
    #phone_number = models.CharField(validators=[phone_regex], blank='True', default='', max_length=9)


    def __unicode__(self):
        return self.report_name