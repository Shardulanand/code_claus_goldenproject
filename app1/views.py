from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
app_name='app1'



def mylogin(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Logged In Successfully!!')
            return redirect('app2:homeurls')
        else:
            messages.error(request,'Something Went Wrong')
            return redirect('app1:myloginurl')
    return render(request,'index.html')


def createuser(request):                                                                              
    if request.method =="POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully!! please Check Your Mail Id')
            return redirect('app1:myloginurl')
        else:
            print(form.errors)
            messages.error(request,'Something Went Wrong')
            return redirect('app1:registerurl')
    return render(request,'app1/register.html')