from django.db import models
from django.contrib.auth.models import AbstractUser # 커스텀 유저를 위한 라이브러리
<<<<<<< HEAD
from django.conf import settings # 외래키를 위한 라이브러리
=======
>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119

# Create your models here.

class User(AbstractUser): #기존 user모델에서 확장되는 형태라 하나만 추가해주면 되어요.
<<<<<<< HEAD
    groupid = models.CharField(max_length=15, blank=True, default='') #그룹아이디를 전달받습니다.
    #username = models.CharField(max_length=15, blank=True)

class Group(models.Model):
    groupid = models.CharField(max_length=15, blank=True, default='')
   # groupid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True,)
    #groupkey =models.CharField(max_length=15, blank=True, default='')
    dogname = models.CharField(max_length=30, blank=True, default='noname')
    dogbirth = models.CharField(max_length=20, blank=True, default='080925' )
    dogbio = models.CharField(max_length=10,blank=True, default='male')
    dogspecies = models.CharField(max_length=30,blank=True, default='nospec')
=======
    groupid = models.CharField(max_length=15, blank=True, default='')
    #username = models.CharField(max_length=15, blank=True)
>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119
