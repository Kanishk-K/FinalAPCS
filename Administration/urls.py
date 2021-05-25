from django.urls import path

from . import views

app_name = 'Administration'
urlpatterns = [
    path('Login/', views.login_view, name='login'),
    path('SignUp/', views.signUp_view, name='signUp'),
    path('LogOut/', views.logout_view, name='logout'),
]