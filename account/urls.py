from django.contrib import admin
from django.urls import path
from account import views  

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'), 
    path('mypage/<str:username>', views.mypage, name = 'mypage'),
    #path('profile/', views.profile, name='profile')
]