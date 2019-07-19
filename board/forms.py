from django import forms
from .models import Posting, Comment

class PostingPost(forms.ModelForm):
        class Meta:
            model = Posting
            fields = ['title','context','image']

