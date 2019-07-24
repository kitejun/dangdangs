from django.db import models
from django.contrib.auth.models import AbstractUser # 커스텀 유저를 위한 라이브러리

# Create your models here.

class User(AbstractUser): #기존 user모델에서 확장되는 형태라 하나만 추가해주면 되어요.
    groupid = models.CharField(max_length=15, blank=True, default='')
    #username = models.CharField(max_length=15, blank=True)