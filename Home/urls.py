from django.urls import path
from . import views  

#To define the urls for the application 
urlpatterns = [
    path('', views.login, name='login'), 
    path('user_registration/', views.registration, name='user_registration'),
    path('user_dashboard/', views.dashboard, name='user_dashboard'),
    path('user_profile/', views.profile, name='user_profile'),
    path('user_eventcreation/', views.eventcreation, name='user_eventcreation'),
    path('user_userregistration/', views.userregistration, name='user_userregistration'),
    path('user_notifications/', views.notifications, name='user_notifications'),
    path('user_dashboard2/', views.dashboard2, name='user_dashboard2'),
    path('user_userregistration2/', views.userregistration2, name='user_userregistration2'),
    
]

