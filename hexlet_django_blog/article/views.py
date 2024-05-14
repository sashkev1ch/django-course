from django.views import View
from django.shortcuts import render, get_object_or_404, redirect

# local
from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import CommentArticleForm, CreateArticleForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, "articles/index.html", context={"articles": articles})


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(request, "articles/article.html", context={"article": article})


class ArticleCommentFormView(View):

    def get(self, request, *args, **kwargs):
        form = CommentArticleForm()  # Создаем экземпляр нашей формы
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request, "articles/comment.html", {"form": form, "article": article}
        )

    def post(self, request, *args, **kwargs):
        form = CommentArticleForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("articles")


class ArticleCreateFormView(View):
    def get(self, request, *args, **kwargs):
        form = CreateArticleForm()
        return render(request, "articles/create.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles")
        
        return render(request, "articles/create.html", context={"form": form})
