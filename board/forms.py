from django import forms
from .models import Board

class BoardPost(forms.ModelForm):
        class Meta:
            model = Board
            fields = ['title','context','image']