from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'class': "form-control",'type':'text','placeholder':'Username','id':"inputUsername"}),
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control",'type':'password','placeholder':'Password','id':"inputPassword"}))
    class Meta:
        model = User
        fields = ('username','password')

class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': "form-control",
            })
        self.fields['password1'].widget.attrs.update({
            'type':'password',
            'placeholder':'Password'
        })
        self.fields['password2'].widget.attrs.update({
            'type':'password',
            'placeholder':'Retype Password'
        })
        self.fields['username'].widget.attrs.update({
            'type':'text',
            'placeholder':'Username'
        })