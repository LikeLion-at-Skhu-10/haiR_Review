from django.shortcuts import render
from django.http import request 

# Create your views here.

#메인페이지
def main(request) :
    return render(request, 'main.html')