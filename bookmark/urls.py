from django.urls import path
import bookmark.views
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView

urlpatterns = [
    path('bookmark_list/', BookmarkListView.as_view(), name='bookmark_list'),
    path('bookmark_create/', BookmarkCreateView.as_view(), name='bookmark_create'),
    path('bookmark_detail/<int:pk>', BookmarkDetailView.as_view(), name='bookmark_detail'),
    path('bookmark_update/<int:pk>', BookmarkUpdateView.as_view(), name='bookmark_update'),
    path('bookmark_delete/<int:pk>', BookmarkDeleteView.as_view(), name='bookmark_delete'),

]