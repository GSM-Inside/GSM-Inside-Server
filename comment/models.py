from django.db import models
from post.models import Post


# Create your models here.
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    password = models.CharField(max_length=50)
    comment = models.CharField(max_length=500)


class SubComment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='subcomments')

    subcomment = models.CharField(max_length=500)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
