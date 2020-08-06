from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(max_length=5000)
    url = models.URLField(max_length=200)
