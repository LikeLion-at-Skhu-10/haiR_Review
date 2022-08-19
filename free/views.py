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
        h_form = HashtagForm (request.POST, instance = hashtag)

        if form.is_valid():
            free = form.save(commit=False)
            free.p_date = timezone.now() 
            free.save()
            
            if form.is_valid() : #게시판 글 작성 후 해시태그 따로 받기 
                hashtag = h_form.save(commit = False) 
                hashtag.p_id = free 
                hashtag.name = h_form.cleaned_data['name']
                hashtag.save()
                h_form.save_m2m()
            return redirect('f_list')

    else:
        form = FreeForm(instance = free)
        h_form = HashtagForm (instance = hashtag)
        return render(request, 'f_write.html', {'form':form, 'h_form':h_form})

#자유게시판 목록
def f_list(request):
    frees = Free.objects
    return render(request, 'f_list.html', {'frees':frees})

#자유게시판 글 / 댓글
def f_detail(request, id):
    free = get_object_or_404(Free, id=id)
    hashtag = get_object_or_404(Hashtag, id = id)

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
        return render(request, 'f_detail.html', {'free':free, 'hashtag' : hashtag, 'form':form})

#자유게시판 수정하기
def f_edit(request, id):
    free = get_object_or_404(Free, id=id)
    hashtag = get_object_or_404(Hashtag, id=id)  

    if request.method == "POST":
        form = FreeForm(request.POST, request.FILES, instance=free)
        h_form = HashtagForm (request.POST, instance = hashtag)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            if h_form.is_valid() : 
                h_form.save(commit=False) 
                h_form.save()
                return redirect('f_list')
    else:
        form = FreeForm(instance=free)
        h_form = HashtagForm (instance=hashtag)
        return render(request, 'f_edit.html', {'form':form, 'h_form':h_form})

#자유게시판 글 수정하기
def f_delete(request, id):
    free = get_object_or_404(Free, id=id)
    free.delete()
    return redirect(f_list)

#해시태그 
# def hashtag(request, hashtag=None) :
#     if request.method == 'POST' :
#         form = HashtagForm(request.POST, instance= hashtag)
#         if form.is_valid() :
#             hashtag = form.save(commit = False)
#             if Hashtag.objects.filter(name=form.cleaned_data['name']) :
#                 form = HashtagForm()
#                 error_message = "이미 존재하는 해시태그 입니다"
#                 return render(request, 'hashtag.html', {'form':form, "error_message":error_message})
#             else :
#                 hashtag.name = form.cleaned_data['name']
#                 hashtag.save()
#             return redirect('f_list')
#     else :
#         form = HashtagForm(instance = hashtag)
#         return render(request, 'hashtag.html', {'form':form})
def f_search(request):
        if request.method == 'POST':
                f_searched = request.POST['f_searched']        
                f_serobj = Free.objects.filter(p_title__contains=f_searched)
                f_serobx = Free.objects.filter(p_body__contains=f_searched)
                return render(request, 'f_search.html', {'f_searched': f_searched,'f_serobj':f_serobj,'f_serobx':f_serobx})
        else:
                return render(request, 'f_search.html', {})