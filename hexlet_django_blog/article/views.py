from django.views import View
from django.shortcuts import render
# local
from hexlet_django_blog.article.models import Article

class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        return render(request, "articles/index.html", context={"articles": articles})

