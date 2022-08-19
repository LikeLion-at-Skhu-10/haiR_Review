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
    return render(request, 'q_list.html' , {'qnaobj':qnaobj})

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


#해시태그 추가하기
# def hashtag(request, hashtag=None) :
#     if request.method == 'POST' :
#        form = HashtagForm(request.POST, instance = hashtag)
#        if form.is_valid() :
#             hashtag = form.save(commit = False)
#             if Hashtag.objects.filter(name=form.cleaned_data['name']) :
#                form = HashtagForm()
#                error_message = "이미 존재하는 해시태그 입니다"
#                return render(request, 'hashtag.html', {'form':form, "error_message":error_message})
#             else :
#                 hashtag.name = form.cleaned_data['name']
#                 hashtag.save()
#                 return redirect('q_list')
#     else:
#         form = HashtagForm(instance = hashtag)
#         return render(request, 'hashtag.html', {'form':form})
def q_search(request):
        if request.method == 'POST':
                q_searched = request.POST['q_searched']        
                q_serobj = Question.objects.filter(question__contains=q_searched)
            
                return render(request, 'q_search.html', {'q_searched': q_searched,'q_serobj':q_serobj})
        else:
                return render(request, 'q_search.html', {})