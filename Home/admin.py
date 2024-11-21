from django.contrib import admin
from .models import *

admin.site.register(Login)
admin.site.register(SignUp) # registers the UserProfile model to make it accessible and manageable through the Django admin interface

# Register your models here.
