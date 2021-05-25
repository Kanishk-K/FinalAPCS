from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from .forms import LoginForm, SignUpForm

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}")
                return redirect('Quizzer:index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = LoginForm()
    return render(request,"Administration/Login.html",context={"form":form})
def signUp_view(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"You are now logged in as {user.username}")
            return redirect('Quizzer:index')
        else:
            messages.error(request, "Invalid username or password.")
    form = SignUpForm()
    return render(request,"Administration/SignUp.html",context={"form":form})

def logout_view(request):
    logout(request)
    messages.success(request, f"You are now logged out.")
    return redirect('Quizzer:index')