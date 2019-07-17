from django import forms
from .models import Board, Comment

class BoardPost(forms.ModelForm):
        class Meta:
            model = Board
            fields = ['title','context','image']

class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ['author','message']