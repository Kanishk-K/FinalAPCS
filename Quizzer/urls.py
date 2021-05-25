from django.urls import path

from . import views

app_name = 'Quizzer'
urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/', views.indexQuiz,name="indexQuiz"),
    path('quiz/<int:id>/',views.startQuiz,name="startQuiz"),
    path('quiz/<int:id>/<int:questionNumber>/',views.quizQuestion,name="quizQuestion"),
]