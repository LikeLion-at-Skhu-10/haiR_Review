from django.shortcuts import render, redirect, get_object_or_404
from main.forms import HashtagForm
from .models import Hashtag
from free.models import Free 
from QnA.models import Question
from review.models import Review
from django.core.paginator import Paginator

# Create your views here.

#메인페이지
def main(request):
    reviews = Review.objects.all().order_by('-r_clicks')[:3]
    qnaobj = Question.objects.all().order_by('-q_clicks')[:3]
    frees = Free.objects.all().order_by('-p_clicks')[:3]
    context = {'reviews':reviews, 'qnaobj':qnaobj, 'frees':frees}
    return render(request, 'main.html', context)

#해시태그 추가하기
def hashtag(request, hashtag=None) :
    if request.method == 'POST' :
        form = HashtagForm(request.POST, instance= hashtag)
        if form.is_valid() :
            hashtag = form.save(commit = False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']) :
                form = HashtagForm()
                error_message = "이미 존재하는 해시태그 입니다"
                return render(request, 'hashtag.html', {'form':form, "error_message":error_message})
            else :
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
            return redirect('h_list')
    else :
        form = HashtagForm(instance = hashtag)
        return render(request, 'hashtag.html', {'form':form})


#해시태그 목록
def h_list(request) :
    hashtags = Hashtag.objects.all()
    return render(request, 'h_list.html', {'hashtags':hashtags})


#전체 검색기능
def m_search(request):
        if request.method == 'POST':
                m_searched = request.POST['m_searched']        
                m_qsearch = Question.objects.filter(question__contains=m_searched)
                m_fsearch = Free.objects.filter(p_title__contains=m_searched)
                m_rsearch = Review.objects.filter(r_title__contains=m_searched)
                return render(request, 'search.html', {'m_searched': m_searched, 'm_qsearch': m_qsearch , 'm_fsearch':m_fsearch , 'm_rsearch':m_rsearch})
        else:
                return render(request, 'search.html', {})