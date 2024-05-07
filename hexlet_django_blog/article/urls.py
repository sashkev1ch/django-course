from django.urls import path
# local
from hexlet_django_blog.article import views


urlpatterns = [
    path("<str:tags>/<int:article_id>/", views.ArticlesView.as_view(), name="tagged_article")
]
