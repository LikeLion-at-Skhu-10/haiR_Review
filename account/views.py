from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.forms import PasswordChangeForm
# jango.contrib.auth 내 함수 login을 import함.
# (views.py 내 정의한 함수 login과 구분하기 위해 auth_log로 재 명명함)

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('main')
        
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            Profile.objects.create(user=user) #프로필 생성
            auth_login(request, user)
            return redirect('main')
    
    else:
        signup_form = UserCreationForm()
    
    return render(request, 'signup.html', {'signup_form': signup_form})

def login(request):
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
        return redirect('main')
    
    else:
        login_form = AuthenticationForm()
    
    return render(request, 'login.html', {'login_form' : login_form})

def logout(request):
    auth_logout(request)
    return redirect('main')

def mypage(request, username):
    #get_user_model() => User 클래스를 호출함
    people = get_object_or_404(get_user_model(), username = username)
    return render(request, 'mypage.html', {'people':people})

def update(request):
    if request.method == 'POST':
        user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_change_form.is_valid():
            user_change_form.save()
            return redirect('mypage',request.user.username)
    else:
            user_change_form = CustomUserChangeForm(instance = request.user)
    return render (request, 'update.html', {'user_change_form':user_change_form})
@login_required
def password(request):
    if request.method == 'POST':
        password_change_form = PasswordChangeForm(request.user, request.POST)
        # 키워드인자명을 함께 써줘도 가능
        # password_change_form = PasswordChangeForm(user=request.user, data=request.POST)
        if password_change_form.is_valid():
            password_change_form.save()
            return redirect('main') 
    else:
        password_change_form = PasswordChangeForm(request.user)
    return render(request, 'password_edit.html',{'password_change_form':password_change_form}) 

def profile_edit(request):
    profile  =request.user.profile
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance = profile)
        if profile_form.is_valid():
            profile_form.save()
        return redirect('mypage' , request.user.username)
    else:
            profile_form = ProfileForm(instance = profile)
    return render(request, 'profile_edit.html' , {'profile_form':profile_form})
        