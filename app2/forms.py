from dataclasses import field
from itertools import product
from django import forms
from app2.models import *

class survey_Form(forms.ModelForm):
    class Meta:
        model=survey
        fields='__all__'

class survey2_Form(forms.ModelForm):
    class Meta:
        model=survey
        fields='__all__'

class report_Form(forms.ModelForm):
    class Meta:
        model=report
        fields='__all__'