from django.db import models
from gallery.models import Gallery
import uuid

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    title = models.CharField(max_length=200)
    content = models.TextField()
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f"{self.gallery.name} {self.title}"


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')

    url = models.CharField(max_length=200)

    def __str__(self):
        return self.post.title
