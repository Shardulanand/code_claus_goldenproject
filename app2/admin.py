from django.contrib import admin
from .models import *




@admin.register(survey)
class survey_admin(admin.ModelAdmin):
    list_display=('Name','Phonenumber','age','occupation','gender','medium','problem','easy','price','comparison')

@admin.register(surveyB)
class survey2_admin(admin.ModelAdmin):
    list_display=('Name','Have_smartphone','which_phone','factors_influence','rating_own_phone','describe_your_phone','Mojor_concern','apps_security','ios_android','occupation')

@admin.register(report)
class report_admin(admin.ModelAdmin):
    list_display=('Name','date','comment')