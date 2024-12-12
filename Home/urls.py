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
    path('mark_notification_read/<int:notification_id>/', views.mark_notifications_as_read, name='mark_notification_read'),

    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

