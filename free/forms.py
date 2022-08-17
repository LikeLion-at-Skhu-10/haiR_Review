from django import forms
from free.models import Free, p_comment
from main.models import Hashtag
from main.views import hashtag

class FreeForm(forms.ModelForm):
    class Meta:
        model = Free 
        fields = ['p_title', 'p_body', 'p_photo', 'hashtags'] 


class p_commentForm(forms.ModelForm):
    class Meta:
        model = p_comment
        fields = ['text']

