from django.db import models

# Create your models here.
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField()

    def __str__(self):
        return self.url