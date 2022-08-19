from django.shortcuts import render, redirect
from django.http import request 

def mypage(request) :
	return render (request, 'mypage.html ') 

