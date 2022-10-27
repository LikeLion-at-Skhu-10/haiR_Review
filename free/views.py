from tkinter.tix import FileSelectBox
from django.shortcuts import render, redirect, get_object_or_404
from free.forms import FreeForm, p_commentForm
from main.forms import HashtagForm 
from django.utils import timezone 
from free.models import Free, p_comment
from main.models import Hashtag 
from django.http import request

# Create your views here.

#자유게시판 작성하기
def f_write(request, free = None, hashtag = None) :
    if request.method == 'POST':
        form = FreeForm(request.POST, request.FILES, instance = free)
        if form.is_valid():
            free = form.save(commit=False)
            free.p_date = timezone.now() 
            free.save()
            form.save_m2m
            return redirect('f_list')

    else:
        form = FreeForm(instance = free)
        h_form = HashtagForm (instance = hashtag)
        return render(request, 'f_write.html', {'form':form, 'h_form':h_form})

#자유게시판 목록
def f_list(request):
    frees = Free.objects
    f_sort = request.GET.get('f_sort', '')
    if f_sort == 'p_clicks' : 
        frees = Free.objects.all().order_by('-p_clicks','-p_date')
    else : 
        frees = Free.objects.all().order_by('-p_date')
    return render(request, 'f_list.html', {'frees':frees, 'f_sort':f_sort})

#자유게시판 글 / 댓글
def f_detail(request, id):
    free = get_object_or_404(Free, id=id)
    if request.method == "POST" :
        form = p_commentForm(request.POST) 
        if form.is_valid() :
            p_comment = form.save(commit = False)
            p_comment.p_id = free
            p_comment.text = form.cleaned_data['text']
            p_comment.save()
            return redirect('f_detail', id)
    else :
        form = p_commentForm()
        return render(request, 'f_detail.html', {'free':free, 'form':form})

#자유게시판 수정하기
def f_edit(request, id):
    free = get_object_or_404(Free, id=id)
    if request.method == "POST":
        form = FreeForm(request.POST, request.FILES, instance=free)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('f_list')
    else:
        form = FreeForm(instance=free)
        return render(request, 'f_edit.html', {'form':form})

#자유게시판 글 수정하기
def f_delete(request, id):
    free = get_object_or_404(Free, id=id)
    free.delete()
    return redirect(f_list)

#좋아요 
def p_likes(request, p_id) : 
    like_b = get_object_or_404(Free_Like, id = p_id) 
    if request.user in like_b.p_like.all() : 
        like_b.p_like.remove(request.user) 
        like_b.p_likes -= 1
        like_b.save() 
    else : 
        like_b.p_like.add(request.user)
        like_b.p_likes += 1 
        like_b.save()
    return redirect('/f_detail/' + str(p_id)) 

#조회수 
# def p_clicks(request, p_id):
#     like_b = get_object_or_404(Free_Clip, id=p_id)
#     if request.user in like_b.p_clip.all():
#         like_b.p_clip.remove(request.user)
#         like_b.p_clicks -= 1
#         like_b.save()
#     else:
#         like_b.p_clip.add(request.user)
#         like_b.p_clicks += 1
#         like_b.save()
#     return redirect('/f_detail/' + str(p_id))

def f_search(request):
        if request.method == 'POST':
                f_searched = request.POST['f_searched']        
                f_serobj = Free.objects.filter(p_title__contains=f_searched)
                f_serobx = Free.objects.filter(p_body__contains=f_searched)
                return render(request, 'f_search.html', {'f_searched': f_searched,'f_serobj':f_serobj,'f_serobx':f_serobx})
        else:
                return render(request, 'f_search.html', {})

