from django.db import models
from authors.models import Author


class Snippet(models.Model):
    author = models.ForeignKey(Author, related_name="snippets")
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
