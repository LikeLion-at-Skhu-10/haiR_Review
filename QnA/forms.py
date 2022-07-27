from django import forms
from .models import QnA , QnAComment, Hashtag #

class QnAForm(forms.ModelForm): #
    class Meta:
        model = QnA #
        fields = ['question','image']
class QnACommentForm(forms.ModelForm):
    class Meta:
        model = QnAComment
        fields = ['text']
class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']        