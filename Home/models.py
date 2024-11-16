from django.db import models

# For the input fields that will be reflected in the server
# Mi dito pwede mo baguhin yung fields if ever, indi kasi ako sure if dapat fields ng registration or login dapat nandito, pero ayon eto yung login fields muna nilagay ko. Sabihan mo ko if babaguhin motong fields para mabago natin sa documentation 

class UserProfile(models.Model):
          
    email = models.EmailField(unique=True)    
    password = models.CharField(max_length=25)  
    

     
