from django.contrib import admin
from django.urls import path
from account import views  

urlpatterns = [
    path('signup/', views.signup, name='signup'), 
    path('login/', views.login, name='login'), 
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='update'),
    path('mypage/<str:username>/', views.mypage, name='mypage'),
    path('password/', views.password, name='password'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    
]