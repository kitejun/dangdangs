from django.contrib import admin
from .models import Board, Comment

# admin 디자인
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id','author', 'title', 'context', 'pub_date', 'hits']

admin.site.register(Board, BoardAdmin)

# admin 디자인
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'comment_body', 'comment_date', 'board']

admin.site.register(Comment, CommentAdmin)