from django.urls import path
# local
from hexlet_django_blog.article import views


urlpatterns = [
    path("", views.index)
]
