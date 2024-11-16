from django.contrib import admin
from .models import *

admin.site.register(UserProfile) # registers the UserProfile model to make it accessible and manageable through the Django admin interface

# Register your models here.
