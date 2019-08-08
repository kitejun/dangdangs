from django.db import models
from django.contrib.auth.models import AbstractUser # 커스텀 유저를 위한 라이브러리
from django.conf import settings # 외래키를 위한 라이브러리

# Create your models here.

class User(AbstractUser): #기존 user모델에서 확장되는 형태라 하나만 추가해주면 되어요.
    groupid = models.CharField(max_length=15, blank=True, default='') #그룹아이디를 전달받습니다.
    #username = models.CharField(max_length=15, blank=True)

class Group(models.Model):
    groupid = models.CharField(max_length=15, blank=True, default='')
   # groupid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True,)
    #groupkey =models.CharField(max_length=15, blank=True, default='')
    dogname = models.CharField(max_length=30, blank=True, default='noname')
    dogbirth = models.CharField(max_length=20, blank=True, default='000000' )
    dogbio = models.CharField(max_length=10,blank=True, default='male')
    dogspecies = models.CharField(max_length=30,blank=True, default='nospec')