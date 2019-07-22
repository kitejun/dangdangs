from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    context=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 최초의 저장된 시간이 저장
    updated_at = models.DateTimeField(auto_now=True) # 매번 저장이 될 때마다 시간이 저장
    image = models.FileField(upload_to="images/%Y/%m/%d", default='https://image.flaticon.com/icons/svg/149/149852.svg')
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.context[:50]

class Comment(models.Model):
    title = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=10)
    message = models.TextField()
    created_at = models.DateTimeField('date published')
    updated_at = models.DateTimeField('date published')
    
    def __str__(self):
        return self.author