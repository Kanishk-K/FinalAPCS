from django.urls import path

from . import views

app_name = 'Quizzer'
urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/', views.indexQuiz,name="indexQuiz"),
    path('quiz/<int:id>/',views.startQuiz,name="startQuiz"),
    path('quiz/<int:id>/<int:questionId>/',views.quizQuestion,name="quizQuestion"),
    path('modify/', views.modifyIndex, name="modifyIndex"),
    path('modify/<int:id>/', views.modifyQuiz ,name="modifyQuiz"),
    path('modify/<int:id>/<int:questionId>/',views.modifyQuestion,name="modifyQuestion"),
    path('delete/<int:id>/', views.deleteQuiz ,name="deleteQuiz"),
    path('delete/<int:id>/<int:questionId>/',views.deleteQuestion,name="deleteQuestion"),
    path('delete/<int:id>/<int:questionId>/<int:choiceId>/',views.deleteChoice,name="deleteChoice"),
    path('fetch/<int:ChoiceID>/',views.AjaxView ,name="AjaxQuiz")
]