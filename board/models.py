from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Board(models.Model):
    title=models.TextField()
    pub_date=models.DateTimeField('date published')
    context=models.TextField()
    like=models.IntegerField(default=0)

    image = models.ImageField(upload_to='images/', default='https://image.flaticon.com/icons/svg/149/149852.svg')
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.context[:100]