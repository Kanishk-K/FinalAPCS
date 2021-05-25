from django.db import models
import os
import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

def upload_Quiz_Image(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Quiz_Image',
        'Quiz_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
)
# Create your models here.
class Quiz(models.Model):
    Subject = models.CharField(max_length=30)
    Description = models.TextField()
    Image = models.ImageField(
        verbose_name=_("Quiz Image"),
        upload_to = upload_Quiz_Image
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    
    class Meta:
        ordering = ['created_at',]
        verbose_name_plural = "Quizzes"
    def __str__(self):
        return self.Subject

class Question(models.Model):
    LinkedQuiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    QuestionNumber = models.IntegerField()
    Prompt = models.CharField(max_length=200)
    Explanation = models.TextField()
    class Meta:
        unique_together = [
            ("LinkedQuiz","QuestionNumber"),
            ("LinkedQuiz","Prompt")
        ]
        ordering = ['QuestionNumber',]
    def __str__(self):
        return str(self.QuestionNumber)

class Choice(models.Model):
    LinkedQuestion = models.ForeignKey(Question,on_delete=models.CASCADE)
    ChoiceNumber = models.IntegerField()
    Text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("LinkedQuestion","Text")
        ]