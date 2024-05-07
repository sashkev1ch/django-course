from django.views import View
from django.shortcuts import render


class ArticlesView(View):
    template_name = "articles/index.html"

    def get(self, request, tags: str, article_id: int):
        return render(request, "articles/index.html", context={"tags": tags, "article_id": article_id})

