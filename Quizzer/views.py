from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hey")
def startQuiz(request,id):
    return HttpResponse("Hey")
def quizQuestion(request,id,questionNumber):
    return HttpResponse("Hey")
