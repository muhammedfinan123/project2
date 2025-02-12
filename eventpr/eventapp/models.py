from django.db import models

# Create your models here.
class Event(models.Model):
    image=models.ImageField(upload_to="pic")
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    def __str__(self):
        return self.name
        
class Booking(models.Model):
    cus_name=models.CharField(max_length=55)
    cus_ph=models.CharField(max_length=12)
    evnt_name=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)