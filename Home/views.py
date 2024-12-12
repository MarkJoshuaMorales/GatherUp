from django.shortcuts import render
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from geopy.geocoders import Nominatim


# Sign Up
@csrf_protect
def registration(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password"]

            user_creds = User.objects.create_user(username=username, email=email, password=password1)
            user_creds.save()

            messages.success(request, "Account created successfully")
            return redirect("login")

        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, "registration.html", {"form": form})

    else:
        form = SignUpForm()

    return render(request, "registration.html", {"form": form})

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_dashboard')  # Redirect to your desired page
        else:
            form.add_error(None, "Invalid username or password")
    elif request.method == 'GET' and 'logout' in request.GET:
        # Logout action
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect('login')  # Redirect to the login page after logout
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Event Creation view
@csrf_protect
@login_required(login_url='login')
def eventcreation(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('user_dashboard')
    else:
        form = EventForm()
    return render(request, "eventcreation.html", {"form": form})

# Dashboard view
@csrf_protect
@login_required(login_url='login')
@login_required
def dashboard(request):
    # Fetch upcoming and past events
    upcoming_events = Event.objects.filter(event_start__gte=timezone.now()).order_by('event_start')
    past_events = Event.objects.filter(event_start__lt=timezone.now()).order_by('-event_start')
    
    created_by = Event.objects.filter(created_by=request.user)

    registered_events = [
        event for event in upcoming_events if event.attendees.filter(id=request.user.id).exists()
    ]

    context = {
        'username': request.user.username,
        'upcoming_events': upcoming_events,
        'upcoming_events_count': upcoming_events.count(),
        'past_events': past_events,
        'past_events_count': past_events.count(),
        'created_by': created_by,
        'registered_events': registered_events,
        'registered_events_count': len(registered_events),
    }
    return render(request, 'dashboard.html', context)

def profile(request):    
    context = {
        
    }
    return render(request, "profile.html", context)


def get_coordinates(address):
    geolocator = Nominatim(user_agent="geoapi")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    return None, None

# Event Details + Registration view
@csrf_protect
@login_required(login_url='login')
def userregistration(request, pk):
    event = Event.objects.get(pk=pk)

    if request.method == 'POST':
        if request.user not in event.attendees.all():
            event.attendees.add(request.user)
            event.save()
            messages.success(request, "You have successfully registered for the event!")
        else:
            messages.warning(request, "You are already registered for this event.")
        return redirect('user_dashboard')
    
    num_attendees = event.registrations.count()
    
    latitude, longitude = get_coordinates(event.event_location)
    
    context = {
        'event': event,
        'latitude': latitude,
        'longitude': longitude,
        'num_attendees': num_attendees
    }
    return render(request, "userregistration.html", context)

def notifications(request):    
    context = {
        
    }
    return render(request, "notifications.html", context)


def userregistration2(request):    
    context = {
        
    }
    return render(request, "userregistration2.html", context)







