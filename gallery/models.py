from django.db import models

# Create your models here.
class Gallery(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    view = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class GalleryRequest(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    date = models.DateTimeField(auto_now_add=True)
