from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Posting(models.Model):
    title=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now=True,blank=False)
    context=models.TextField()
    image = models.FileField(upload_to="board/%Y/%m/%d", default='C:\Github\dangdangs\media\images\dog2.png')


    def __str__(self):
        return self.title

    def summary(self):
        return self.context[:100]


class Comment(models.Model):
    title = models.ForeignKey(Posting, on_delete=models.CASCADE)
    author = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.author