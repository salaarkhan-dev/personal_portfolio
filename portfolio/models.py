from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200, blank=True)
    date = models.DateField()