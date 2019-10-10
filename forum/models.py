from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    question = models.CharField("Pergunta", max_length=1000)
    answer = models.TextField("Resposta", blank=True, null=True)
    requester = models.ForeignKey(
        User,
        verbose_name="Solicitado por",
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name="requester")
    answered_by = models.ForeignKey(
        User,
        verbose_name="Respondido por",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="answered_by")
    created_at = models.DateTimeField("Criado em", auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em", auto_now=True)
    answered = models.BooleanField("Respondido?", default=False)

    class Meta:
        verbose_name = "Pergunta"
        verbose_name_plural = "Perguntas"

    def __str__(self):
        return f"{self.question}"

    def formater_request(self):
        full_name = " ".join([self.requester.first_name, self.requester.last_name])
        formated = ".".join([y[:1] for y in full_name.split(" ")])
        return formated
