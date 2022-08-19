from django import forms
from .models import Hashtag

class HashtagForm(forms.ModelForm) : 
    class Meta :
        model = Hashtag
        fields = ['name']