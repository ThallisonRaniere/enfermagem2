from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login/',
         auth_views.LoginView.as_view(template_name="home/login.html"),
         name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('cadastro/', views.Registration.as_view(), name="registration"),
    path('sobre/', views.AboutView.as_view(), name="about"),
    path('sucesso/',
        TemplateView.as_view(template_name="home/success.html"),
        name="user_created")
]
