import requests

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, TemplateView

from .forms import UserCreateForm
from .models import About, Profile
from article.models import Article

class Home(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(show=True)
        return context


class Login(TemplateView):
    template_name = "home/login.html"


class Registration(FormView):
    template_name = "home/registration.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("user_created")

    def recaptcha(self, token):
        secret_key = settings.RECAPTCHA
        url = "https://www.google.com/recaptcha/api/siteverify?secret={}&response={}".format(
            secret_key, token
        )
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        result = requests.post(url, headers=headers)
        if result.json().get('success') and result.json().get('score') >= 0.5:
            return True
        else:
            return False

    def form_valid(self, form):
        if self.recaptcha(form.data.get('token')):
            with transaction.atomic():
                user = User.objects.create(
                    username=form.data.get('username'),
                    first_name=form.data.get('first_name'),
                    last_name=form.data.get('last_name'))
                user.set_password('654321')
                user.save()
                profile = Profile.objects.create(user=user, age=int(form.data.get('age')))
                return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form, msg="Atualize a página e tente novamente. Error:RCP")

    def form_invalid(self, form, msg=None):
        return self.render_to_response(self.get_context_data(form=form, msg=msg))


class AboutView(TemplateView):
    template_name = "home/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context
