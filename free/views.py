from tkinter.tix import FileSelectBox
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm, p_commentForm, HashtagForm
from django.utils import timezone
from .models import Blog, p_comment, Hashtag
from django.http import request

# Create your views here.
def f_write(request, blog = None) :
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.p_date = timezone.now() 
            blog.save()
            form.save_m2m()
            return redirect('main')
    else:
        form = BlogForm(instance = blog)
        return render(request, 'f_write.html', {'form':form})

def f_list(request):
    blogs = Blog.objects
    return render(request, 'f_list.html', {'blogs':blogs})

def f_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == "POST" :
        form = p_commentForm(request.POST) 
        if form.is_valid() :
            comment = form.save(commit = False)
            comment.blog_id = blog
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('f_detail', id)
    else :
        form = p_commentForm()
        return render(request, 'f_detail.html', {'blog':blog, 'form':form})

def f_edit(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('f_list')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'f_edit.html', {'form':form})

def f_delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.delete()
    return redirect(f_list)

def f_hashtag(request, hashtag=None) :
    if request.method == 'POST' :
        form = HashtagForm(request.POST, instance= hashtag)
        if form.is_valid() :
            hashtag = form.save(commit = False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']) :
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다"
                return render(request, 'f_hashtag.html', {'form':form, "error_message":error_message})
            else :
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('f_list')
    else :
        form = HashtagForm(instance = hashtag)
        return render(request, 'f_hashtag.html', {'form':form})