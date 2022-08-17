from email.policy import default
from django.shortcuts import render, redirect, get_object_or_404
from review.forms import ReviewForm, r_commentForm
from main.forms import HashtagForm
from django.utils import timezone
from review.models import Review, r_comment
from main.models import Hashtag
from django.http import request

# Create your views here.

#리뷰 작성
def r_write(request, review = None) :
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance = review)

        if form.is_valid():
            review = form.save(commit=False)
            review.r_date = timezone.now() 
            review.save()
            form.save_m2m()
                
            return redirect('r_list')
    else:
        form = ReviewForm(instance = review)
        return render(request, 'r_write.html', {'form':form })

#리뷰 목록
def r_list(request):
    reviews = Review.objects
    #default_r_clikes = blogs.r_clikes
    # blogs.r_clikes = default_r_clikes +1
    return render(request, 'r_list.html', {'reviews':reviews})

#리뷰 글 상세페이지
def r_detail(request, id):
    review = get_object_or_404(Review, id=id)

    if request.method == "POST" :
        form = r_commentForm(request.POST)
        if form.is_valid() :
            comment = form.save(commit = False)
            comment.r_id = review
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect('r_detail', id)
            
    else :
        form = r_commentForm()
        return render(request, 'r_detail.html', {'review':review, 'form':form})

#리뷰 수정
def r_edit(request, id):
    review = get_object_or_404(Review, id=id)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            return redirect('r_list')
    else:
        form = ReviewForm(instance=review)
        return render(request, 'r_edit.html', {'form':form})

#리뷰 삭제
def r_delete(request, id):
    review = get_object_or_404(Review, id=id)
    review.delete()
    return redirect('r_list')

#해시태그
# def r_hashtag(request, hashtag=None) :
#     if request.method == 'POST' :
#         form = HashtagForm(request.POST, instance= hashtag)
#         if form.is_valid() :
#             hashtag = form.save(commit = False)
#             if Hashtag.objects.filter(name=form.cleaned_data['name']) :
#                 form = HashtagForm()
#                 error_message = "이미 존재하는 해시태그 입니다"
#                 return render(request, 'r_hashtag.html', {'form':form, "error_message":error_message})
#             else :
#                 hashtag.name = form.cleaned_data['name']
#                 hashtag.save()
#             return redirect('r_list')
#     else :
#         form = HashtagForm(instance = hashtag)
#         return render(request, 'r_hashtag.html', {'form':form})
def r_search(request):
        if request.method == 'POST':
                r_searched = request.POST['r_searched']        
                r_serobj = Review.objects.filter(r_title__contains=r_searched)
                return render(request, 'r_search.html', {'r_searched': r_searched,'r_serobj':r_serobj})
        elif request.method == 'POST' :
                r_searched = request.POST['r_searched']        
                r_serobj = Review.objects.filter(r_date__contains=r_searched)
                return render(request, 'r_search.html', {'r_searched': r_searched,'r_serobj':r_serobj})
        else:       
                return render(request, 'r_search.html', {})
#for문 안에서 r db를 찾을 때 까지 돌고 제목,본문내용 둘 중 하나라도 들어가면 출력 둘 다 없으면, 없음 출력 or Q사용 나중에 유지보수하자..
