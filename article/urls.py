from django.urls import path

from .views import ArticleDetailView

urlpatterns = [
    path('artigo/<str:slug>/', ArticleDetailView.as_view(), name="article_detail"),
]