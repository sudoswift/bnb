from django.db import models
from django.contrib.auth.models import AbstractUser

# About DATA
# Create your models here.
# '''를 class 아래에 써주면 view나 admin에서 볼 때 밑에 설명에 각주가 뜬다.

class User(AbstractUser):
    '''Custom User Model'''
    
    GENDER_MALE = "M" # 여기의 male, female, other은 실제 DB가 인식하는 부분
    GENDER_FEMALE = "FE"
    GENDER_OTHER = "O"
    
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'), # 'male'은 choices의 picker에 나타나는 부분
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other'),
        
    ]
    
    LANGUAGE_ENGLISH = "EN"
    LANGAUGE_KOREAN = "KR"
    
    LANGUAGE_CHOICES =[
        (LANGUAGE_ENGLISH, 'English'),
        (LANGAUGE_KOREAN, 'Korean'),
    ]
    
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    
    CURRENCY_CHOICES = [
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
    ]
    
    avatar = models.ImageField(null = True, blank = True) #null은 form에서 입력할 때 작용하고, blank는 실제 DB에서 작동한다.
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6, null = True, blank = True, default=GENDER_MALE)
    bio = models.TextField(default= "", blank = True)
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True)
    superhost = models.BooleanField(default=False)
    
