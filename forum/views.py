from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .forms import QuestionCreateForm
from .models import Question


class QuestionCreateView(LoginRequiredMixin, CreateView):
    template_name = "forum/form.html"
    form_class = QuestionCreateForm
    success_url = reverse_lazy("question_created")

    def get_initial(self):
        initial = super().get_initial()


class QuestionListView(LoginRequiredMixin, ListView):
    template_name = "forum/list.html"
    model = Question
    queryset = Question.objects.filter(answered=True, answer__isnull=False).order_by("created_at")
    context_object_name = "questions"
