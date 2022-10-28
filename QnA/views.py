from django.shortcuts import render , redirect ,get_object_or_404
from .forms import QuestionForm, AnswerForm
from main.forms import HashtagForm 
from django.utils import timezone
from QnA.models import Question, Answer 
from main.models import Hashtag
from django.http import request
# Create your views here.

#질문 작성
def q_write(request, qna = None):
        if request.method == 'POST':
            form = QuestionForm(request.POST, request.FILES,instance = qna)
            if form.is_valid():
                    qna = form.save(commit=False)
                    qna.q_date = timezone.now()
                    qna.save()
                    form.save_m2m()
                    return redirect('q_list')
        else:
            form = QuestionForm (instance= qna)
            return render(request, 'q_write.html' , {'form':form})

#질문 목록
def q_list(request):
    qnaobj = Question.objects
    q_sort = request.GET.get('q_sort','') #정렬
    if q_sort == 'q_clicks' :
        qnaobj = Question.objects.all().order_by('-q_clicks','-q_date')
    else :
        qnaobj = Question.objects.all().order_by('-q_date')
    return render(request, 'q_list.html' , {'qnaobj':qnaobj, 'q_sort':q_sort})

#질문글 상세페이지
def q_detail(request, id):
    qna = get_object_or_404(Question, id=id)
    if request.method == "POST" :
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid() :
            answer = form.save(commit = False)
            answer.qna_id = qna
            answer.text = form.cleaned_data['text']
            answer.save()
            form.save_m2m()
            return redirect('q_detail' , id)
    else :
        form = AnswerForm()
        return render(request, 'q_detail.html' , {'qna' : qna , 'form':form})

#질문 수정하기
def q_edit(request , id):
        qna = get_object_or_404(Question, id=id)
        if request.method == "POST":
            form = QuestionForm(request.POST, request.FILES, instance=qna)
            if form.is_valid():
                    form.save(commit=False)
                    form.save()
                    return redirect('q_list')
        else:
            form = QuestionForm(instance=qna)
            return render(request, 'q_edit.html' , {'form':form})

#질문 삭제
def q_delete(request, id):
    qna = get_object_or_404(Question, id=id)           
    qna.delete()
    return redirect('q_list')

#좋아요 
def q_likes(request, id):
    like_b = get_object_or_404(Question, id=id)
    if request.nickname in like_b.q_like.all(): #nickname 
        like_b.q_like.remove(request.nickname)
        like_b.q_likes -= 1
        like_b.save()
    else:
        like_b.q_like.add(request.nickname)
        like_b.q_likes += 1
        like_b.save()
    return redirect('/q_detail/' + str(id))

#추천수 
# def q_clip(request, id):
#     like_b = get_object_or_404(Question, id=id)
#     if request.q_user in like_b.q_clip.all(): #q_user
#         like_b.q_clip.remove(request.q_user)
#         like_b.q_clips -= 1
#         like_b.save()
#     else:
#         like_b.q_clip.add(request.q_user)
#         like_b.q_clips += 1
#         like_b.save()
#     return redirect('/q_detail/' + str(id))

#검색하기
def q_search(request):
        if request.method == 'POST':
                q_searched = request.POST['q_searched']        
                q_serobj = Question.objects.filter(question__contains=q_searched)
                return render(request, 'q_search.html', {'q_searched': q_searched,'q_serobj':q_serobj})
        else:
                return render(request, 'q_search.html', {})
