from django.shortcuts import render
from django.views.generic.list import ListView
# Create your views here.

from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

def list(request):
    return render(request, 'bookmark/list.html')