from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

class Article(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name="Autor",
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name="author")
    title = models.CharField(
        "Título", max_length=300, blank=False, null=False)
    description = models.TextField("Descrição", blank=False, null=False)
    content = models.TextField("Conteúdo", blank=False, null=False)
    created_at = models.DateTimeField(
        "Criado em", auto_now_add=True)
    updated_at = models.DateTimeField(
        "Atualizado em", auto_now=True)
    show = models.BooleanField("Mostrar", default=True)
    slug = models.SlugField(max_length=500, editable=False, null=True, blank=True)

    class Meta:
        verbose_name = "Artigo"
        verbose_name_plural = "Artigos"

    def __str__(self):
        return f"{self.title}"

    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super().save(*args, **kwargs)

    @property
    def get_author(self):
        return self.author.first_name
