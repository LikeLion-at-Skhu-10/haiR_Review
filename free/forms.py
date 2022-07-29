from django import forms
from .models import Blog, p_comment, Hashtag

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['p_title', 'p_body', 'p_photo', 'hashtags']

class p_commentForm(forms.ModelForm):
    class Meta:
        model = p_comment
        fields = ['text']

class HashtagForm(forms.ModelForm) :
    class Meta :
        model = Hashtag
        fields = ['name']

