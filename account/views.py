from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

#회원가입
def signup(request) : 
    if request.method == 'POST' :
        form = UserCreationForm(request.POST) 
        if form.is_valid() : 
            user = form.save() 
            auth.login(request, user) 
            return redirect('main')
        else : 
            return render(request, 'signup.html', {'form':form})
    else : 
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})

#로그인
def login(request) :
    if request.method == 'POST' : 
        form = AuthenticationForm(data = request.POST)
        if form.is_valid() : 
            user = form.save() 
            auth.login(request, user) 
            return redirect('main')
        else : 
            return render(request, 'login.html', {'form':form})
    else : 
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

#로그아웃
def logout(request) :
    auth.logout(request) 
    return redirect('main')