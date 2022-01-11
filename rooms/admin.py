from django.contrib import admin
from . import models

@admin.register(models.RoomType)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Amenity)
class AmenityAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass

@admin.register(models.HouseRule)
class HouseRule(admin.ModelAdmin):
    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass