from django import forms
from .models import Board

class BoardPost(forms.ModelForm):
        class Meta:
            model = Board
            fields = ['title','context','image']

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='검색')