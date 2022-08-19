from typing_extensions import Required
from django.contrib.auth.forms import UserChangeForm 
from .models import Profile, User

class CustomUserChangeForm(UserChangeForm) :
    password = None 

    class Meta :
        model = User 
        fields = ['username', 'email'] 


class ProfileForm(models.Model) :
    nickname = forms.CharField(label = "닉네임", required=False) 
    profile_Img = forms.ImageField(lable = "프로필 사진", required=False) 

    class Meta : 
        model = Profile 
        fields = ['nickname', 'profile_Img'] 