from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('forum/cadastro/', views.QuestionCreateView.as_view(), name='question_create'),
    path(
        'forum/cadastro/sucesso/',
        TemplateView.as_view(template_name="forum/success.html"),
        name='question_created'),
    path('forum/perguntas/', views.QuestionListView.as_view(), name='questions'),
]