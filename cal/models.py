from django.db import models
from django.urls import reverse

TODO_CHOICES = (
    ('사료', '사료'),
    ('산책', '산책'),
    ('쇼핑', '쇼핑'),
    ('병원', '병원'),
)

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    # 종류 선택 list
    todo = models.CharField(max_length=4,choices=TODO_CHOICES, default='사료')
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('cal:event_detail', args = (self.id,)) # 캘린더 상의 일정을 누르면 detail 페이지로 이동
        return f'<a href="{url}"> {self.title} </a>'

    def __str__(self):
        return self.title


