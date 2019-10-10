from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name="Usuário",
        on_delete=models.CASCADE)
    age = models.PositiveIntegerField("Idade", blank=False, null=False)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

    def __str__(self):
        return f"{self.user} {self.age} anos"


class About(models.Model):
    content = models.TextField("Conteúdo", blank=False, null=False)

    class Meta:
        verbose_name = "Sobre"
        verbose_name_plural = "Sobre"


    def __str__(self):
        return f"{self.content[:30]}..."