from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserCredential(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_image = models.ImageField(upload_to='events/', null=True, blank=True, default='events/Rectangle 2.png')
    event_start= models.DateTimeField()
    event_end = models.DateTimeField()
    event_location = models.CharField(max_length=255)
    event_description = models.TextField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_private = models.BooleanField(default=False)
    event_capacity = models.PositiveIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events', null=True)
    attendees = models.ManyToManyField(User, related_name='registered_events')

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
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True, default='profile_pics/Generic avatar.png')

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.recipient.username}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()