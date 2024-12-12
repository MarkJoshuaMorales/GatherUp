from django.urls import path
from . import views  
from django.conf import settings
from django.conf.urls.static import static

#To define the urls for the application 
urlpatterns = [
    path('', views.login_view, name='login'), 
    path('user_registration/', views.registration, name='user_registration'),
    path('user_dashboard/', views.dashboard, name='user_dashboard'),
    path('user_profile/', views.profile, name='user_profile'),
    path('user_eventcreation/', views.eventcreation, name='user_eventcreation'),
    path('event/<int:pk>/', views.userregistration, name='user_userregistration'),
    path('user_notifications/', views.notifications, name='user_notifications'),
    path('user_userregistration2/', views.userregistration2, name='user_userregistration2'), 
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

