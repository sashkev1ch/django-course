from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


def about(request):
    return render(request, "about.html")
