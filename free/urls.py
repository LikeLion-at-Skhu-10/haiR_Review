from django.contrib import admin
from django.urls import path
from free import views  

urlpatterns = [
    path('f_write/', views.f_write, name = 'f_write'),
    path('f_list/', views.f_list, name='f_list'),
    path('f_detail/<str:id>/', views.f_detail, name='f_detail'),
    path('f_edit/<str:id>/', views.f_edit, name='f_edit'),
    path('f_delete/<str:id>/', views.f_delete, name='f_delete'),
    path('p_like/<int:p_id>/', views.p_likes, name="p_likes"),
    #path('p_clicks/<int:p_id>/', views.p_clicks, name="p_clicks"),
]