from django import forms
from .models import Blog, r_comment, Hashtag

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['r_title','r_body', 'r_name', 'r_location', 'r_photo', 'r_receipt', 'r_nickname', 'hashtags' ]

class r_commentForm(forms.ModelForm) :
    class Meta :
        model = r_comment
        fields = ['text']

class HashtagForm(forms.ModelForm) :
    class Meta :
        model = Hashtag
        fields = ['name']

