from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Quiz, Question, Choice
from .forms import QuizForm, QuestionForm, ChoiceForm
from django.contrib import messages

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
def quizQuestion(request,id,questionId):
    return HttpResponse("Hey")

def modifyIndex(request):
    if request.method == "POST":
        form = QuizForm(request.POST,request.FILES)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.last_modified = request.user
            quiz.save()
            return redirect(f"Quizzer:modifyQuiz",id=quiz.id)
        else:
            context = {
                "Quizzes":Quiz.objects.all(),
                "form": form
            }
            messages.warning(request, 'Form contents were not valid to be entered into the database.')
            return render(request,'Quizzer/modifyIndex.html',context=context)
    else:
        context = {
            "Quizzes":Quiz.objects.all(),
            "form":QuizForm()
        }
        return render(request,'Quizzer/modifyIndex.html',context=context)

def modifyQuiz(request,id):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.LinkedQuiz = Quiz.objects.get(id=id)
            question.save()
            return redirect(f"Quizzer:modifyQuestion",id=id,questionId=question.id)
        else:
            context = {
                "Quiz" : Quiz.objects.get(id=id),
                "Questions" : Quiz.objects.get(id=id).question_set.all(),
                "form":form
                }
            messages.warning(request, 'Form contents were not valid to be entered into the database.')
            return render(request,'Quizzer/modifyQuiz.html',context=context)
    else:
        context = {
            "Quiz" : Quiz.objects.get(id=id),
            "Questions" : Quiz.objects.get(id=id).question_set.all(),
            "form" : QuestionForm()
        }
        return render(request,'Quizzer/modifyQuiz.html',context=context)

def modifyQuestion(request, id, questionId):
    if request.method == "POST":
        form = ChoiceForm(request.POST)
        if form.is_valid():
            choice = form.save(commit=False)
            choice.LinkedQuestion = Question.objects.get(id=questionId)
            choice.save()
            context = {
                "Quiz" : Quiz.objects.get(id=id),
                "Question" : Question.objects.get(id=questionId),
                "Choices" : Question.objects.get(id=questionId).choice_set.all(),
                "form":ChoiceForm()
            }
            return render(request,"Quizzer/modifyQuestion.html",context=context)
        else:
            context = {
                "Quiz" : Quiz.objects.get(id=id),
                "Questions" : Question.objects.get(id=questionId),
                "Choices" : Question.objects.get(id=questionId).choice_set.all(),
                "form":form
            }            
            messages.warning(request, 'Form contents were not valid to be entered into the database.')
            return render(request,"Quizzer/modifyQuestion.html",context=context)
    else:
        context = {
            "Quiz" : Quiz.objects.get(id=id),
            "Question" : Question.objects.get(id=questionId),
            "Choices" : Question.objects.get(id=questionId).choice_set.all(),
            "form":ChoiceForm()
        }
        return render(request,'Quizzer/modifyQuestion.html',context=context)

def deleteQuiz(request, id):
    QuizObject = Quiz.objects.get(id=id)
    QuizObject.delete()
    return redirect("Quizzer:modifyIndex")


def deleteQuestion(request, id, questionId):
    QuestionObject = Question.objects.get(id=questionId)
    QuestionObject.delete()
    return redirect("Quizzer:modifyQuiz",id=id)

def deleteChoice(request, id, questionId, choiceId):
    ChoiceObject = Choice.objects.get(id=choiceId)
    ChoiceObject.delete()
    return redirect("Quizzer:modifyQuestion",id=id,questionId=questionId)