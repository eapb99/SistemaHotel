from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator,MaxValueValidator


class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    hotel_name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, null = True, blank=True) 
    stars_rating = models.SmallIntegerField(
        validators= [MinValueValidator(1),MaxValueValidator(5)]
    )
    num_rooms = models.SmallIntegerField()
    postal_code = models.CharField(max_length=10,null=True, blank=True)



    def __str__(self):
        return f"{self.hotel_id}: {self.hotel_name} -- {self.country}"


class RoomType(models.Model):
    room_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    num_beds = models.SmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # is_vip = models.BooleanField()

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_type = models.ForeignKey(RoomType,on_delete=models.DO_NOTHING)
    hotel = models.ForeignKey(Hotel,on_delete=models.DO_NOTHING)
    code = models.CharField(max_length=5)
    is_available = models.BooleanField()

    def __str__(self):
        return f"{self.code} {self.hotel}"