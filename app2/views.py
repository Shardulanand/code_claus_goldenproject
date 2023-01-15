from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
app_name='app2'


def home(request):
    countinst=survey.objects.all().count()
    occinst=survey.objects.filter(occupation='student').count()
    geninst=survey.objects.filter(gender='male').count()
    geninst_female=survey.objects.filter(gender='female').count()
    mobile=survey.objects.filter(medium='mobile').count()
    website=survey.objects.filter(medium='website').count()
    comparisoninst=survey.objects.filter(comparison='zomato').count()
    comparisonswiggy=survey.objects.filter(comparison='swiggy').count()
    reportinst=report.objects.all()
    count_surevy2=surveyB.objects.all().count()
    count_smartphone_yes=surveyB.objects.filter(Have_smartphone='Yes').count()
    occuinst_surveyb=surveyB.objects.filter(occupation='business').count()
    factors_influence=surveyB.objects.filter(factors_influence='build quality').count()
    Mojor_concern=surveyB.objects.filter(Mojor_concern='battery health').count()
    rating_own_phone=surveyB.objects.filter(rating_own_phone='10').count()
    ios_android=surveyB.objects.filter(ios_android='ios').count()
    which_phone=surveyB.objects.filter(which_phone='apple').count()

    context={
        'countinst':countinst,
        'occinst':occinst,
        'geninst':geninst,
        'geninst_female':geninst_female,
        'mobile':mobile,
        'website':website,
        'comparisoninst':comparisoninst,
        'comparisonswiggy':comparisonswiggy,
        'reportinst':reportinst,
        'count_surevy2':count_surevy2,
        'count_smartphone_yes':count_smartphone_yes,
        'occuinst_surveyb':occuinst_surveyb,
        'factors_influence':factors_influence,
        'Mojor_concern':Mojor_concern,
        'rating_own_phone':rating_own_phone,
        'ios_android':ios_android,
        'which_phone':which_phone,
    }
    return render(request,'app2/home.html',context)

def survey1(request):
    if request.method =="POST":
        form=survey_Form(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            return redirect('app2:homeurls')
    form=survey_Form()
    context={
        'form':form,
    }
    return render(request,'app2/survey1.html',context)

def survey2(request):
    if request.method =="POST":
        form=survey2_Form(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            return redirect('app2:homeurls')
    form=survey2_Form()
    context={
        'form':form,
    }
    return render(request,'app2/survey2.html',context)


def userresponse(request):
    surveyinst= survey.objects.all()
    context={
        'surveyinst': surveyinst,
    }
    return render(request,'app2/useresponse.html',context)

def viewsurvey(request):
    return render(request,'app2/viewsurvey.html')

def viewresponse(request):
    return render(request,'app2/viewresponse.html')

def userresponse2(request):
    surveyinst2= surveyB.objects.all()
    context={
        'surveyinst2': surveyinst2,
    }
    return render(request,'app2/useresponse2.html',context)

def createreport(request):
    if request.method =="POST":
        form=report_Form(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
            return redirect('app2:homeurls')
    form=report_Form()
    context={
        'form':form,
    }
    return render(request,'app2/createsurveyreport.html',context)

def downloadreport(request):
    return render(request,'app2/downloadreport.html')