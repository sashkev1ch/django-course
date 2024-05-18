from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages import get_messages, info

# local
from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import CommentArticleForm, CreateArticleForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        messages = get_messages(request)
        return render(request, "articles/index.html", context={"articles": articles, "messages": messages})


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
            # messages.add_messge(request, messages.INFO, "Article added")
            info(request, "Article added")
            return redirect("articles")

        return render(request, "articles/create.html", context={"form": form})


class IndexArtickeUpdateView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs["id"]
        article = Article.objects.get(id=article_id)
        form = CreateArticleForm(instance=article)
        return render(request, "articles/update.html", context={"form": form, "article_id": article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs["id"]
        article = Article.objects.get(id=article_id)
        form = CreateArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("articles")

        return render("articles/update.html", context={"form": form, "article_id": article_id})
