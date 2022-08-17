from django.contrib import admin
from django.urls import path
from QnA import views  

urlpatterns = [
    path('q_write/', views.q_write, name = 'q_write'),
    path('q_list/', views.q_list, name='q_list'),
    path('q_detail/<str:id>/', views.q_detail, name='q_detail'),
    path('q_edit/<str:id>/', views.q_edit, name='q_edit'),
    path('q_delete/<str:id>/', views.q_delete, name='q_delete'),
    path('q_search/', views.q_search, name='q_search'),
    #path('q_hashtag/', views.q_hashtag, name='q_hashtag'),
]