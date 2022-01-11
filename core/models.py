from django.db import models


# 많은 장고 앱들의 모델 중에서 겹치는 놈들을 core라는 앱을 따로 만들어서 관리가 편하게 해주는 기능이다. class 안에 또다른 Meta 라는 클래스를 만들어서 abstract = True를 넣어준다. 이 모델은 어떠한 데이타베이스의 테이블도 만들지 않는다.
class TimeStampedModel(models.Model):
    """Time Stamped Model"""
    created = models.DateTimeField(auto_now_add=True) #auto_now_add 는 첫 생성시 저장되는 갱신되지 않는 정보
    updated = models.DateTimeField(auto_now=True)# auto_now는 갱신가능한 정보, DateTimeField와 DateField 에서 사용가능
    
    class Meta:
        abstract = True