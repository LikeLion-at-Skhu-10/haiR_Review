from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from .models import Profile
from django import forms 

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name','last_name']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'introduction', 'p_image']