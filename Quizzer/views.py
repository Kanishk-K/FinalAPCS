from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz, Question, Choice

# Create your views here.
def index(request):
    return render(request,'index.html')
def indexQuiz(request):
    context = {
        "Quizzes":Quiz.objects.all()
    }
    return render(request,'Quizzer/indexQuiz.html',context=context)
def startQuiz(request,id):
    return HttpResponse("Hey")
def quizQuestion(request,id,questionNumber):
    return HttpResponse("Hey")
