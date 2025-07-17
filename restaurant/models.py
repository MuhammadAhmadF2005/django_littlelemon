from django.db import models


# Create your models here.
class Booking(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   guest_number = models.IntegerField()
   comment = models.CharField(max_length=1000)

   def __str__(self):
      return self.first_name + ' ' + self.last_name


# Add code to create Menu model

class Menu(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    description=models.CharField(max_length=1000, default="")

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menu"

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name
   