# import 할 때에는 1순위: 파이썬, 2순위: 장고, 3순위: 써드파티앱, 4순위: 내가 만든 앱 순으로 써야한다.
from django.db import models 
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models

class AbstractItem(core_models.TimeStampedModel):
    """Abstract Item"""
    name = models.CharField(max_length=80)
    
    class Meta:
        abstract= True
        
    def __str__(self):
        return self.name
    
class RoomType(AbstractItem):
    """RoomType Object Definition"""
    class Meta:
        verbose_name_plural = "Room Types"

# verbose_name_plural
class Amenity(AbstractItem):
    """Amenity Model Definition"""
    class Meta:
        verbose_name_plural = "Amenities"
        
class Facility(AbstractItem):
    """Facility Model Definition"""
    class Meta:
        verbose_name_plural = "Facilities"

class HouseRule(AbstractItem):
    """HouseRule Model Definition"""
    class Meta:
        verbose_name_plural = "House Rules"


class Room(core_models.TimeStampedModel):
    """Room Model Definition"""
     
    name = models.CharField(max_length=140, blank=True)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140, blank = True)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)# ForeignKey는 이미 있는 model(database)를 다른 model에 연동시키는 것임!! many-to-one relationship 이다.
    room_type = models.ForeignKey(RoomType, on_delete = models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)
    
    def __str__(self):
        return self.name