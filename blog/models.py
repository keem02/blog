from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def has_been_updated(self):
        # updated_at이 created_at보다 나중인 경우만 True
        return self.updated_at > self.created_at

    def __str__(self):
        return self.title
