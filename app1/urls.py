from django.urls import path
from .views import *
app_name='app1'

urlpatterns = [
    path('',mylogin,name='myloginurl'),
    path('createuser/',createuser,name='registerurl'),
]
