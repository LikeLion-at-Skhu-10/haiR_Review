from email.policy import default
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogForm, r_commentForm, HashtagForm
from django.utils import timezone
from .models import Blog, r_comment, Hashtag
from django.http import request

# Create your views here.
def r_write(request, blog = None) :
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance = blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.r_date = timezone.now() 
            blog.save()
            form.save_m2m()
            return redirect('r_list')
    else:
        form = BlogForm(instance = blog)
        return render(request, 'r_write.html', {'form':form})

def r_list(request):
    blogs = Blog.objects
    sort = request.GET.get('sort','')
    if sort == 'r_clicks':
        blogs = Blog.objects.all().order_by('-r_clicks','-r_date')
    else:
        blogs = Blog.objects.all().order_by('-r_date')

    return render(request, 'r_list.html', {'blogs':blogs, 'sort':sort})

def r_detail(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.method == "POST" :
        form = r_commentForm(request.POST)
        if form.is_valid() :
            comment = form.save(commit = False)
            comment.blog_id = blog
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('r_detail', id)
            
    else :
        form = r_commentForm()

        return render(request, 'r_detail.html', {'blog':blog, 'form':form})


def r_edit(request, id):
    blog = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('r_list')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'r_edit.html', {'form':form})

def delete(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.delete()
    return redirect('r_list')

def r_hashtag(request, hashtag=None) :
    if request.method == 'POST' :
        form = HashtagForm(request.POST, instance= hashtag)
        if form.is_valid() :
            hashtag = form.save(commit = False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']) :
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다"
                return render(request, 'r_hashtag.html', {'form':form, "error_message":error_message})
            else :
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('r_list')
    else :
        form = HashtagForm(instance = hashtag)
        return render(request, 'r_hashtag.html', {'form':form})

def r_likes(request, blog_id):
    like_b = get_object_or_404(Blog, id=blog_id)
    if request.user in like_b.r_like.all():
        like_b.r_like.remove(request.user)
        like_b.r_likes -= 1
        like_b.save()
    else:
        like_b.r_like.add(request.user)
        like_b.r_likes += 1
        like_b.save()
    return redirect('/r_detail/' + str(blog_id))

def r_clip(request, blog_id):
    like_b = get_object_or_404(Blog, id=blog_id)
    if request.user in like_b.r_clip.all():
        like_b.r_clip.remove(request.user)
        like_b.r_clips -= 1
        like_b.save()
    else:
        like_b.r_clip.add(request.user)
        like_b.r_clips += 1
        like_b.save()
    return redirect('/r_detail/' + str(blog_id))
