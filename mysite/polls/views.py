from django.http import HttpResponse
from django.http import  HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from .models import Question, Choice


#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def polls_main(request):
    print(request.user)
    #return HttpResponse("Hello, polls_main")
    return render(request, 'base.html')

def index(request):
    print(request.user)
    print(Question.objects.order_by('-pub_date')[:5])
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/list.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    try:
        selected_question = Question.objects.get( id = question_id )
        latest_choice = Choice.objects.filter(question_id = question_id)[:10]        
        latest_choice_text = Choice.objects.filter(question_id = question_id).values_list('choice_text')[:10]
        latest_choice_votes = Choice.objects.filter(question_id = question_id).values_list('votes')[:10]
    except:
        raise Http404("Нет материалов")
    return render (request,'polls/detail.html', {'selected_question': selected_question, 'latest_choice': latest_choice,  'latest_choice_text': latest_choice_text,  'latest_choice_votes': latest_choice_votes, } )

def leave_comment(request, question_id):
    try:
        a = Question.objects.get( id = question_id )
    except: 
         raise Http404("Нет материалов")
    a.choice_set.create(choice_text = request.GET['choice_text'], votes  = request.GET['votes'])
    return  HttpResponseRedirect( reverse('polls:detail', args = (a.id,)) )
