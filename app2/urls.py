from django.urls import path
from app2.views import *
app_name='app2'

urlpatterns = [
    path('home/',home,name='homeurls'),
    path('survey1/',survey1,name='survey1urls'),
    path('userresponse/',userresponse,name='userresponseurls'),
    path('userresponse2/',userresponse2,name='userresponse2urls'),
    path('viewsurveys/',viewsurvey,name='viewsurveyurls'),
    path('survey2/',survey2,name='survey2urls'),
    path('viewresponse/',viewresponse,name='viewresponseurls'),
    path('createreport/',createreport,name='createreporturls'),
    path('downloadreport/',downloadreport,name='downloadreporturls'),
]
