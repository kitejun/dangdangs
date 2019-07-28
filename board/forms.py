from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
        class Meta:
            model = Post
            fields = ['title','context','image']

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='검색')

class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ['author','message']