from django.db import models
from django.conf import settings # 외래키를 위한 라이브러리

# Create your models here.

class Board(models.Model):
    #author = models.ForeignKey( on_delete=models.CASCADE, settings.AUTH_USER_MODEL)
    title=models.TextField()
    image = models.FileField(upload_to="images/%Y/%m/%d", default='https://image.flaticon.com/icons/svg/149/149852.svg')
    pub_date=models.DateTimeField('date published')
    context=models.TextField()
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.context[:100]

class Comment(models.Model):
    # author = models.ForeignKey(Board, settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    board = models.ForeignKey(Board, null=True, related_name='comments')   
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_body = models.CharField(max_length=50)