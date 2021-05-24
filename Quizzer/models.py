from django.db import models

# Create your models here.
class Quiz(models.Model):
    Subject = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    
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
        return self.QuestionNumber

class Choice(models.Model):
    LinkedQuestion = models.ForeignKey(Question,on_delete=models.CASCADE)
    Text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    class Meta:
        unique_together = [
            ("LinkedQuestion","Text")
        ]