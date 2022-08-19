from django.contrib import admin
from django.urls import path
from review import views  

urlpatterns = [
    path('r_write/', views.r_write, name = 'r_write'),
    path('r_list/', views.r_list, name='r_list'),
    path('r_detail/<str:id>/', views.r_detail, name='r_detail'),
    path('r_edit/<str:id>/', views.r_edit, name='r_edit'),
    path('r_delete/<str:id>/', views.r_delete, name='r_delete'),
    path('r_like/<int:r_id>/', views.r_likes, name="r_likes"),
    #path('r_clip/<int:r_id>/', views.r_clip, name="r_clips"),
    path('r_search/', views.r_search, name='r_search'),
]