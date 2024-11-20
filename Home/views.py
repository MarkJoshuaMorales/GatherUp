from django.shortcuts import render
from .forms import *

def login(request):
    form = AddUserProfileForm()
    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def registration(request):    
    context = {
        
    }
    return render(request, "registration.html", context)

def dashboard(request):    
    context = {
        
    }
    return render(request, "dashboard.html", context)

def profile(request):    
    context = {
        
    }
    return render(request, "profile.html", context)

def eventcreation(request):    
    context = {
        
    }
    return render(request, "eventcreation.html", context)

def userregistration(request):    
    context = {
        
    }
    return render(request, "userregistration.html", context)

def notifications(request):    
    context = {
        
    }
    return render(request, "notifications.html", context)






