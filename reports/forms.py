from django import forms
from django.core.exceptions import ValidationError
from models import Report



class ReportForm(forms.ModelForm):

    class Meta:
        model = Report
        exclude = []
