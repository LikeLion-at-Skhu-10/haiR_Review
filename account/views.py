from multiprocessing import context
from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from django.contrib import auth 
from django.contrib.auth import login, authenticate, logout 
from account.forms import AccountAuthForm, RegisterForm

# Create your views here.

#회원가입 
def signup(request, *args, **kwargs) :
    user = request.user 
    if user.is_authenticated : 
        return HttpResponse("이미 존재하는 계정 입니다" + user.username) 

    context = { }
    if request.POST : 
        form = RegisterForm(request.POST) 
        if form.is_valid() :
            form.save() 
            username = form.cleaned_data.get('username').lower() 
            raw_password = form.cleaned_data('password1')
            account = authenticate(username=username, password=raw_password) 
            login (request, account) 
            #destiantion = kwargs.get("next")
            destination = get_redirect_if_exists(request) 
            if destination :
                return redirect(destination)
            return redirect('main') 
        else : 
            context['registration_form'] = form 
    else : 
        form = RegisterForm 
        context['registration_form'] = form

    return render(request, 'signup.html', context) 


#로그아웃
def logout(request) :
    logout(request) 
    return redirect('main') 


#로그인
def login(request, *args, **kwargs) :
    
    context = { }

    user = request.user
    if user.is_authenticated : 
        return redirect('main') 

    destination = get_redirect_if_exists(request) 
    if request.POST : 
        form = AccountAuthForm(request.POST) 
        if form.is_valid() :
            username = request.POST.get('username') 
            password = request.POST.get('password') 
            user = authenticate(username = username, password=password) 
            if user : 
                login(request, user)
                if destination :
                    return redirect(destination) 
            return redirect('main') 
    else : 
        form = AccountAuthForm 

    context['login_form'] = form 

    return render(request, 'login.html', context) 


def get_redirect_if_exists(request) : 
    redirect = None 
    if request.GET : 
        if request.GET.get("next") :
            redirect = str(request.GET.get("next")) 
    return redirect 