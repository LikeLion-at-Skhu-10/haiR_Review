from django.urls import path
import bookmark.views
from .views import BookmarkListView

urlpatterns = [
    path('list/' , bookmark.views.list, name='list'),

]