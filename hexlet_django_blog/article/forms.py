from django.forms import ModelForm, CharField
from hexlet_django_blog.article.models import ArticleComment, Article

class CommentArticleForm(ModelForm):
    content = CharField(max_length=100)

    class Meta:
        model = ArticleComment
        fields = ["content"]


class CreateArticleForm(ModelForm):
    name = CharField(max_length=200)
    body = CharField(max_length=1000)

    class Meta:
        model = Article
        fields = ["name", "body"]
