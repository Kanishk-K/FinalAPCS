from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import Quiz, Question, Choice

class QuizForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': "form-control",
            })
    class Meta:
        model = Quiz
        fields = ['Subject','Description','Image']

class QuestionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': "form-control",
            })
    class Meta:
        model = Question
        fields = ['QuestionNumber',"Prompt","Explanation"]

class ChoiceForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': "form-control",
            })
    class Meta:
        model = Choice
        fields = ['ChoiceNumber',"Text","is_correct"]