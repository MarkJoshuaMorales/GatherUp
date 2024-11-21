from django.db import models
from django.contrib.auth.hashers import make_password

# For the input fields that will be reflected in the server
# Mi dito pwede mo baguhin yung fields if ever, indi kasi ako sure if dapat fields ng registration or login dapat nandito, pero ayon eto yung login fields muna nilagay ko. Sabihan mo ko if babaguhin motong fields para mabago natin sa documentation 

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
