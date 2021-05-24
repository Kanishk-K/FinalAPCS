from django.urls import path

from . import views

app_name = 'Data'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/',views.startQuiz,name="startQuiz"),
    path('<int:id>/<int:questionNumber>/',views.quizQuestion,name="quizQuestion"),
]