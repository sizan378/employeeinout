from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import *
from django.utils import timezone

from .models import *




def index(request):
    # user= User.objects.all()
    user=Attend.objects.all()
    return render(request, 'profile.html', {'user':user})
    

def getLogin(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == "POST":
            user = request.POST.get('username')
            password = request.POST.get('password')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('profile')
    return render(request, "login.html")

def getLogout(request):
    logout(request)
    return redirect('login')


def attend(request):
    status = None
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                attended_datetime = str(timezone.now())[:10]
                
            except:
                pass

     
            attended_today = Attend.objects.filter(attender=request.user, datetime__startswith=attended_datetime)
                
            if str(attended_today)[10:] == "[]>":
                status = 3
            else:
                status = 2

            if status == 3:
                attend_object = Attend(attender=request.user)
                attend_object.save()
                status = 1
        else:
            status = 0

    return render(request, 'attend.html',{'status':status})


def OutTime(request):

    status = None
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                attended_datetime = str(timezone.now())[:10]
            except:
                pass

     
            attended_today = Outtime.objects.filter(outtimmer=request.user, datetime__startswith=attended_datetime)
            if str(attended_today)[10:] == "[]>":
                status = 3
            else:
                status = 2

            if status == 3:
                attend_object = Outtime(outtimmer=request.user)
                attend_object.save()
                status = 1
        else:
            status = 0

    return render(request, 'outtime.html',{'status':status})
    


