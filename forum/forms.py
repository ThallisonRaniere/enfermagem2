from django import forms

from .models import Question

class QuestionCreateForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['question', 'requester']
        widgets = {
            'question': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Escreva aqui a sua pergunta."
            }),
            'requester': forms.HiddenInput()
        }
