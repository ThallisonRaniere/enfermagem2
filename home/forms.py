from django import forms
from django.contrib.auth.models import User


class UserCreateForm(forms.Form):
    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    age = forms.CharField(max_length=2)


    def clean_username(self):
        user = self.cleaned_data.get('username')
        if User.objects.filter(username=user).exists():
            self.add_error(
            	field="username",
            	error="O usuário informado já está sendo usado por outra pessoa, escolha outro por favor.")
            return user