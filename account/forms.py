
import email
from email.policy import EmailPolicy
from django import forms 
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.contrib.auth import authenticate 
from account.models import User 

#유저 생성 폼
class RegisterForm(UserCreationForm) : 
    email = forms.EmailField(max_length=200, help_text='정확한 이메일 주소를 입력하세요')

    class Meta : 
        model = User 
        fields = ['username', 'name', 'email', 'password1', 'password2'] 

    def clean_username(self) :
        username = self.cleaned_data['username'] 
        try: 
            user = User.objects.get(username = username) 
        except Exception as e :
            return username 
        raise forms.ValidationError("이미 존재하는 ID 입니다")

    def clean_email(self) :
        EmailPolicy = self.cleaned_data['email'] 
        try: 
            user = User.objects.get(email = email) 
        except Exception as e :
            return email 
        raise forms.ValidationError("이미 사용되고 있는 이메일 입니다")


#로그인 인증 폼
class AccountAuthForm(forms.ModelForm) :
    password = forms.CharField(label = 'password', widget = forms.PasswordInput)
    
    class Meta :
        model = User
        fields = ['username', 'password']

    def clean(self) :
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password) :
                raise forms.ValidationError("아이디 혹은 비밀번호가 틀렸습니다") 


#유저 수정 폼 
class UserChangeForm (forms.ModelForm) :
    password = ReadOnlyPasswordHashField 

    class Meta : 
        model = User 
        fields = ('username', 'password', 'is_active', 'is_admin') 

    def clean_password(self) :
        return self.initial["password"]
