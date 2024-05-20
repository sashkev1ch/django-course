from django.urls import path
# local
from hexlet_django_blog.article import views


urlpatterns = [
    path("", views.IndexView.as_view(), name="articles"),
    path("<int:id>/comment/", views.ArticleCommentFormView.as_view(), name="comment_create"),
    path("<int:id>/edit/", views.IndexArtickeUpdateView.as_view(), name="edit_article"),
    path("<int:id>/delete/", views.ArticleDeleteView.as_view(), name="article_delete"),
    path("<int:id>/", views.ArticleView.as_view(), name="article"),
    path("create", views.ArticleCreateFormView.as_view(), name="create_article")
]
