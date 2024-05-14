from django.forms import ModelForm
from hexlet_django_blog.article.models import ArticleComment, Article

class CommentArticleForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ["content"]


class CreateArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["name", "body"]
