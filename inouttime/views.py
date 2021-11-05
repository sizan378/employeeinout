from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import *
from django.utils import timezone

from .models import *
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity



def index(request):
    # user= User.objects.all()
    # x_form_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_form_for is not None:
    #     ip = x_form_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')

    # print("Yours IP Address:",ip)
    user=Attend.objects.all().order_by('datetime__minute')
    out = Outtime.objects.all().order_by('datetime__minute')


    return render(request, 'index.html', {'user':user, 'out':out})
    

def getLogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('username')
            password = request.POST.get('password')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                ip, ip_routable = get_client_ip(request)

                if ip is None :
                    ip = "0.0.0.0"
                try:
                    response = DbIpCity.get(ip, api_key='free')
                    country = response.country + " | " + response.city
                except:
                    country="Unknown"
                
                b = EmployeeIP(ip=ip,country=country)
                b.save()
                return redirect('index')

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

def getSupport(request):
    form = SupportForm(request.POST or None)
    u=get_object_or_404(author, name=request.user.id)
    
    print(u)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.employee=u 
        instance.save()
        return redirect('index')
    return render(request,'support.html',{'form':form})



    


