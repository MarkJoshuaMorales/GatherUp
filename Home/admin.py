# admin.py
from django.contrib import admin
from .models import *

<<<<<<< HEAD
=======
admin.site.register(Login)
admin.site.register(SignUp) # registers the UserProfile model to make it accessible and manageable through the Django admin interface
>>>>>>> 22888e62d16f943bfe66b6993d6b8d67f7db578f

admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(Profile)
