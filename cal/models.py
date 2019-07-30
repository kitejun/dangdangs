from django.db import models
from django.urls import reverse
from datetime import datetime
<<<<<<< HEAD
from django.utils import timezone
# from django.contrib.auth.models import User
from django.conf import settings
=======
>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119

TODO_CHOICES = (
    ('사료', '사료'),
    ('산책', '산책'),
    ('쇼핑', '쇼핑'),
    ('병원', '병원'),
    ('목욕', '목욕'),
)

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    # 종류 선택 list
<<<<<<< HEAD
    todo = models.CharField(max_length=5,choices=TODO_CHOICES, default='사료')
    context = models.TextField() # 용어 통일 : description -> context
    start_date = models.DateField(default=timezone.now) # start_time -> start_date, Datetime -> DateField
    end_time = models.DateTimeField(auto_now=True) # end_time -> update time, 갱신시 자동 update
    # idname = models.ForeignKey(User, on_delete=models.CASCADE, )  # User table의 id 참조(ForeignKey), CASCADE => user id 업데이트 시 얘도 변경됨
    groupid = models.CharField(max_length=15, blank=True, default='')
=======
    todo = models.CharField(max_length=4,choices=TODO_CHOICES, default='사료')
    description = models.TextField()
    start_time = models.DateTimeField(default=datetime.now(), blank=True)
    end_time = models.DateTimeField(default=datetime.now(), blank=True)
>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119

    @property
    def get_html_url(self):
        url = reverse('cal:event_detail', args = (self.id,)) # 캘린더 상의 일정을 누르면 detail 페이지로 이동
        return f'<a href="{url}"> {self.title} </a>'
<<<<<<< HEAD
        
=======
>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119

    def __str__(self):
        return self.title

<<<<<<< HEAD
class Daily(models.Model):
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=200)
    count = models.IntegerField(default=0)
    groupid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,) 


=======
>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119

