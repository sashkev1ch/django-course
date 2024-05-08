from django.forms import ModelForm
from hexlet_django_blog.article.models import ArticleComment

class CommentArticleForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ["content"]
