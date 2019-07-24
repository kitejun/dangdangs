from django.db import models
from django.urls import reverse
from datetime import datetime
from django.utils import timezone



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
    todo = models.CharField(max_length=5,choices=TODO_CHOICES, default='사료')
    context = models.TextField() # 용어 통일 : description -> context
    start_date = models.DateField(default=timezone.localtime()) # start_time -> start_date, Datetime -> DateField
    end_time = models.DateTimeField(auto_now=True) # end_time -> update time, 갱신시 자동 update
    # User table의 id 참조(ForeignKey), CASCADE => user id 업데이트 시 얘도 변경됨
    # idname = models.ForeignKey(User, on_delete=models.CASCADE, ) 

    @property
    def get_html_url(self):
        url = reverse('cal:event_detail', args = (self.id,)) # 캘린더 상의 일정을 누르면 detail 페이지로 이동
        return f'<a href="{url}"> {self.title} </a>'
        

    def __str__(self):
        return self.title


