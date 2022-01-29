from django.db import models
from django.db.models import (
    Model, DateTimeField)

from users.models import User


class TrackableDate(Model):
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(TrackableDate):
    title = models.CharField(max_length=255)
    link = models.URLField(max_length=200)
    amount_of_votes = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=True, blank=True)
    voted_by = models.ManyToManyField(User)

    def __str__(self):
        return "{} | {}".format(self.title, self.author)

    class Meta:
        app_label = 'core'
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-created_at',)


class Comment(TrackableDate):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{} | {}".format(self.post, self.author)

    class Meta:
        app_label = 'core'
        verbose_name = 'Коммент'
        verbose_name_plural = 'Комменты'
        ordering = ('-created_at',)
