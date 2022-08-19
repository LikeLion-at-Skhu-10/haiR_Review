from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
# Create your views here.

from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark



class BookmarkCreateView(CreateView) :
    model = Bookmark
    fields = ['site_name', 'url']
    success_url= reverse_lazy('bookmark_list')
    template_name_suffix = '_create'

def bookmark_create(request):
    return redirect('bookmark/list.html')

class BookmarkDetailView(DetailView):
    model = Bookmark

def detail(request):
    return render(request,'bookmark/datail.html')

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url= reverse_lazy('bookmark_list')
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url= reverse_lazy('bookmark_list')