from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):
    """Review Model Definition"""
    
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    # ForeignKey에서 가져온 모델의 Field의 모델의 Field 값들에 접근을 해서 그 값을 admin으로 가져올 수 있다!! 또한 그 Model의 Field가 또 ForeignKey라면(ForeignKey의 ForeignKey 값) 그 값 또한 가져올 수 있다!!
    def __str__(self):
        # Model 에서 두가지 이상의 field 값을 admin 패널에서 보여주고 싶다면 pyhton3의 f-string formate을 이용해 두가지 이상의 값을 가져올 수 있다람쥐.
        return f'{self.review} - {self.room}'