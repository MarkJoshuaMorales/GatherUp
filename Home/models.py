from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User
=======
from django.contrib.auth.hashers import make_password
>>>>>>> 22888e62d16f943bfe66b6993d6b8d67f7db578f

class UserCredential(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)

<<<<<<< HEAD
    def __str__(self):
        return self.username
=======
class Login(models.Model):
    email = models.EmailField(unique=True)    
    password = models.CharField(max_length=255)

    def validate_user(self):
        try:
            user = SignUp.objects.get(email=self.email)
        except SignUp.DoesNotExist:
            raise ValueError('User does not exist')
        
        if not user.check_password(self.password):
            raise ValueError('Invalid password')  
>>>>>>> 22888e62d16f943bfe66b6993d6b8d67f7db578f
    
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_image = models.ImageField(upload_to='events/', null=True, blank=True)
    event_start= models.DateTimeField()
    event_end = models.DateTimeField()
    event_location = models.CharField(max_length=255)
    event_description = models.TextField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_private = models.BooleanField(default=False)
    event_capacity = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events', null=True)
    attendees = models.ManyToManyField(User, related_name='registered_events')

<<<<<<< HEAD
    class Meta:
        db_table = 'Home_event'

    def __str__(self):
        return self.event_name
    
class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Home_registration'

    def __str__(self):
        return f'{self.user.username} registered for {self.event.title}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
=======
class SignUp(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)

    def check_password(self):
        if self.password != self.confirm_password:
            raise ValueError('Passwords does not match')
        
    def save(self, *args, **kwargs):
        self.check_password()
        
        self.password = make_password(self.password)

        super(SignUp, self).save(*args, **kwargs)
>>>>>>> 22888e62d16f943bfe66b6993d6b8d67f7db578f
