from django.shortcuts import render
from django.db.models import query
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth  import authenticate,  login
from django.http import HttpResponse
import attendence
from attendence.models import ApplyLeave,Time
from django.contrib.auth.models import User
from datetime import date, datetime, time
from django.utils.timezone import utc

superusers = User.objects.filter(is_superuser=True)

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            if user in superusers:
                auth.login(request, user)
                return redirect("admin")
            else:
               auth.login(request, user)
               return redirect("display")
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')    

def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save();
                print('user created')
                return redirect('display',user)

        else:
            messages.info(request,'password not matching..')    
            return redirect('signup')
        return redirect('/')
        
    else:
        return render(request,'signup.html')

def display(request):

    now = datetime.now()
    timesheet = Time.objects.create(clockin=now)
    
    return render(request,'display.html',{'timesheet':timesheet})

def admin(request):
    
    return render(request,'admin.html')


def leave(request):
    if request.method == 'POST':
        name = request.POST['name']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        leave = ApplyLeave.objects.create(name=name,startdate=startdate,enddate=enddate)
        leave.save()
        return redirect('display')
    return render(request,'leave.html')

def leave_action(request):
    all_leaves = ApplyLeave.objects.all()

    return render(request,'leave_action.html',{'all_leaves':all_leaves})

def logout(request):
    
    auth.logout(request)
    return render('login.html')

def timesheet(request):
    attendence = Time.objects.all()
    return render(request,'timesheet.html',{'attendence':attendence})

def clockout(request):
        clockout = datetime.now()
        timesheet = Time.objects.create(clockout=clockout)
        return render(request,'display.html',{'timesheet':timesheet})