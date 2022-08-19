from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from account.forms import CustomUserChangeForm ,ProfileForm
from account.models import Profile

# Create your views here.

#회원가입
def signup(request):
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if request.POST["password1"] == request.POST["password2"]:
                    user = User.objects.create_user(
                    username = request.POST["username"],
                    password = request.POST["password1"]
                    )
                    nickname = request.POST["nickname"],
                    email = request.POST["email"],
                    p_num = request.POST["p_num"]
                    profile = Profile(user=user, nickname=nickname, email=email, p_num= p_num )
                    profile.save()
                    auth.login(request, user)
                    return redirect('main')
            else:
            
                    return render(request, 'signup.html' , {'form':form})
    else:        
        form = UserCreationForm()
        return render(request, 'signup.html' , {'form':form})


#로그인 
def login(request):
    if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                    user = form.get_user()
                    auth.login(request, user)
                    return redirect('main')
            else:
            
                    return render(request, 'login.html' , {'form':form})
    else:        
        form = AuthenticationForm()
        return render(request, 'login.html' , {'form':form})


#로그아웃 
def logout(request) :
    auth.logout(request)
    return redirect('main')

#마이페이지
def mypage(request, username) :
        profile = get_object_or_404(User, username = username) 
        return render(request, 'mypage.html', {'profile':profile})


#프로필 수정하기
# def profile(request) :
#         if request.method == 'POST' :
#                 user_change_form = CustomUserChangeForm(request.POST, instance = request.user)
#                 profile_form = ProfileForm(request.POST, request.Files, instance = request.user.profile) 

#                 if user_change_form.is_valid() and profile_form.is_valid() :
#                         user = user_change_form.save()
#                         profile_form.save() 
#                         return redirect('profile', user.username)
                
#                 return redirect('profile', user.username) 
#         else : 
#                 user_change_form = CustomUserChangeForm(instance = request.user) 
#                 profile, create = Profile.objects.get_or_create(user = request.user)
#                 profile_form = ProfileForm(instance = profile) 
#                 return render (request, 'profile.html', {'user_change_form':user_change_form, 'profile_form':profile_form})