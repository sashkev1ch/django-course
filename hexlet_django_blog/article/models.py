from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

# Create your models here.
