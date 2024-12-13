from django.shortcuts import render
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from geopy.geocoders import Nominatim
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import *



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


            profile, created = Profile.objects.get_or_create(user=user_creds)


            if created and not profile.profile_pic:
                profile.profile_pic = 'profile_pics/Generic avatar.png'
                profile.save()

            messages.success(request, "Account created successfully")
            return redirect("login")
        else:
            messages.error(request, "Please correct the errors below.")
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
            return redirect('user_dashboard')
        else:
            form.add_error(None, "Invalid username or password")
    elif request.method == 'GET' and 'logout' in request.GET:
        # Logout action
        logout(request)
        messages.success(request, "You have been logged out.")
        return redirect('login')
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

            other_users = User.objects.exclude(id=request.user.id)
            for user in other_users:
                Notification.objects.create(
                    recipient=user,
                    message=f"{request.user.username} has created a new event: {event.event_name}"
                )
            
            return redirect('user_dashboard')
    else:
        form = EventForm()
    return render(request, "eventcreation.html", {"form": form})

# Dashboard view
@csrf_protect
@login_required(login_url='login')
@login_required
def dashboard(request):
    upcoming_events = Event.objects.filter(event_start__gte=timezone.now()).order_by('event_start')
    past_events = Event.objects.filter(event_start__lt=timezone.now()).order_by('-event_start')
    profile = Profile.objects.get(user=request.user)
    
    created_by = Event.objects.filter(created_by=request.user)
    created_events_count = Event.objects.filter(created_by=request.user).count()

    registered_events = [
        event for event in upcoming_events if event.attendees.filter(id=request.user.id).exists()
    ]

    registered_events_count = len(registered_events)

    context = {
        'username': request.user.username,
        'upcoming_events': upcoming_events,
        'upcoming_events_count': upcoming_events.count(),
        'past_events': past_events,
        'past_events_count': past_events.count(),
        'created_by': created_by,
        'profile': profile,
        'created_events_count': created_events_count,
        'registered_events': registered_events,
        'registered_events_count': registered_events_count,
    }
    return render(request, 'dashboard.html', context)

@csrf_protect
@login_required(login_url='login')
def profile(request):    
    profile = Profile.objects.get(user=request.user)
    created_events_count = Event.objects.filter(created_by=request.user).count()
    registered_events_count = Event.objects.filter(attendees=request.user).count()
    

    if request.method == 'POST':
        if 'delete_account' in request.POST:
            user = request.user
            user.delete()
            messages.success(request, "Your account has been deleted successfully.")
            return redirect('login')

        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if 'clear' in request.POST:
            profile.profile_pic = None 
            profile.save()
            return redirect('user_profile')

        if form.is_valid():
            form.save()
            return redirect('user_profile')

    else:
        form = ProfileForm(instance=profile)


    context = {
        'form': form,
        'date_joined': request.user.date_joined,
        'user' : request.user,
        'profile': profile,
        'created_events_count': created_events_count,
        'registered_events_count': registered_events_count
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
    host_profile = get_object_or_404(Profile, user=event.created_by)
    registered = request.user in event.attendees.all()

    if request.method == 'POST':
        if request.user not in event.attendees.all():
            event.attendees.add(request.user)
            event.save()
            Notification.objects.create(
                    recipient=event.created_by,
                    message=f"{request.user.username} has registered for your event: {event.event_name}"
                )
            messages.success(request, "You have successfully registered for the event!")
        else:
            messages.warning(request, "You are already registered for this event.")
        return redirect('user_userregistration', pk=pk)

    num_attendees = event.attendees.count()

    profile = Profile.objects.get(user=request.user)
    
    latitude, longitude = get_coordinates(event.event_location)
    
    context = {
        'event': event,
        'latitude': latitude,
        'longitude': longitude,
        'num_attendees': num_attendees,
        'profile': profile,
        'host_profile': host_profile.profile_pic,
        'registered': registered
    }
    return render(request, "userregistration.html", context)

# Notification view
@csrf_protect
@login_required(login_url='login')
def notifications(request):    
    notifications = Notification.objects.filter(recipient=request.user)
    unread_count = notifications.filter(is_read=False).count()

    context = {
        'notifications': notifications,
        'unread_count': unread_count
    }
    return render(request, "notifications.html", context)


@csrf_exempt
@login_required
def mark_notifications_as_read(request):
    try:
        notification_id = request.POST.get('notification_id')
        notification = Notification.objects.get(id=notification_id, recipient=request.user)
        notification.is_read = True
        notification.save()
        return JsonResponse({"status": "success"})
    except Notification.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Notification not found"}, status=404)



