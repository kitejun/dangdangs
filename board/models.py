from django.db import models
from django.conf import settings # 외래키를 위한 라이브러리

# Create your models here.

class Board(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title=models.TextField()
    image = models.FileField(upload_to="images/%Y/%m/%d", default='https://image.flaticon.com/icons/svg/149/149852.svg')
    pub_date=models.DateTimeField('date published')
    context=models.TextField()
    hits=models.PositiveIntegerField(default=0)
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_users')
    
    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.title

    def summary_title(self):
        return self.title[:20]

    def summary(self):
        return self.context[:100]

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', args=[self.id])

    @property
    def update_counter_hit(self):
        self.hits=self.hits+1
        self.save()
        return ''

    @property
    def update_counter(self):
        self.like=self.like+1
        self.save()

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='comments')   
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_body = models.CharField(max_length=50)

    def __str__(self):
        return self.author, self.comment_body
    
    class Meta:
        ordering=['-id']