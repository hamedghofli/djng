from django.db import models

# Create your models here.


class mbr (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    
    def __str__(self):
        return "first name: "+self.first_name +" last name: "+ self.last_name + ' email:'+self.email