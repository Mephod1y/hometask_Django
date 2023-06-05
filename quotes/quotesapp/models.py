from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255, blank=False)
    birthday = models.DateTimeField(max_length=25, blank=False)
    born = models.CharField(max_length=25, blank=False)
    description = models.CharField(max_length=150, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'fullname'], name='author of username')
        ]

    def __str__(self):
        return f"{self.fullname}"


class Tag(models.Model):
    tag = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return f"{self.tag}"


class Quote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    quote = models.TextField(null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes', blank=False)
    tags = models.ManyToManyField(Tag, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'quote'], name='quote of username')
        ]

    def __str__(self):
        return f"{self.quote}"
