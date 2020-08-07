from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='blog/images/')
    tags = models.CharField(max_length=20)

    def __str__(self):
        return self.title
