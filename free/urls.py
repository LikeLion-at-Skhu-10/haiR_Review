from django.contrib import admin
from django.urls import path
from free import views  

urlpatterns = [
    path('f_write/', views.f_write, name = 'f_write'),
    path('f_list/', views.f_list, name='f_list'),
    path('f_detail/<str:id>/', views.f_detail, name='f_detail'),
    path('f_edit/<str:id>/', views.f_edit, name='f_edit'),
    path('f_delete/<str:id>/', views.f_delete, name='f_delete'),
    #path('f_hashtag/', views.f_hashtag, name='f_hashtag'),
]