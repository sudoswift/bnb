from django.contrib import admin
from . import models

#여기서 list_display 할 때는 register 한 Model이 여러개 니까 def 에서 obj.rooms.count()로 해준다.
@admin.register(models.RoomType,models.Amenity,models.Facility,models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """Item Admin Definition"""
    
    list_display = (
        "name",
        "used_by",
    )
    
    def used_by(self,obj):
        return obj.rooms.count()
    
    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """Room Admin Definition"""
    
    # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets
    fieldsets = (
        ("Basic Info", {
            "fields": (
                "name", "description", "country", "address", "price"
            ),
        }),
        ("Times",{
            "fields": (
                "check_in", "check_out", "instant_book"
            ),
        }),
        ("Spaces",{
            "fields": (
                "guests", "beds", "bedrooms", "baths"
            ),
        }),
        ("More Spaces",{
            'classes': ('collapse',), # classes를 사용해서 admin 에서 보기/감추기 기능을 삽입할 수 있다.
            "fields": (
                "amenities", "facilities", "house_rules"
            ),
        }),
        ("Last Details",{
            "fields": (
                "host",
            ),
        }),
    )
    
    
    
    #admin 페이지에서 아래 튜플에 있는 Model의 field 값들을 리스트로 나뉘어서 표현해준다.
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
    )
    
    # # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.ordering
    # ordering = ['-name', '-price', '-bedrooms']
    
    #admin 페이지 오른 쪽에 아래 튜플에 있는 Model 의 field 값들의 필터를 만들어 준다.
    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )
    
    # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields
    # ForeignKey나 ManyToMany 를 이용해 만들어놓은 Model의 field 값을 admin에 가져오고 싶다면 __언더스코어두개를 붙이면 된다.
    search_fields = [
        'city', "^host__username"
    ]
    
    # https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.filter_horizontal
    filter_horizontal = [
        "amenities",
        "facilities",
        "house_rules",
    ]
    
    #이거를 Adming Custom이라고 부른다
    # 이 함수에서 self는 RoomAdmin, obj는 현재의 row를 뜻한다.
    def count_amenities(self, obj):
        return  obj.amenities.count()
    
    def count_photos(self, obj):
        return obj.photos.count()
    
    

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """Photo Admin Definition"""
    pass


# QuerySet : https://docs.djangoproject.com/en/4.0/ref/models/querysets/