from django.shortcuts import render, redirect
from .forms import HashtagForm
from .models import Hashtag
from .models import Review
from .models import Free
from .models import Question
from django.core.paginator import Paginator  

# Create your views here.s

def main(request):
    reviews = Review.objects.all().order_by('-r_clicks')[:3]
    qnaobj = Question.objects.all().order_by('-q_clicks')[:3]
    frees = Free.objects.all().order_by('-p_clicks')[:3]
    context = {'reviews':reviews, 'qnaobj':qnaobj, 'frees':frees}
    return render(request, 'main.html', context)

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
            return redirect('f_list')
    else :
        form = HashtagForm(instance = hashtag)
        return render(request, 'hashtag.html', {'form':form})
