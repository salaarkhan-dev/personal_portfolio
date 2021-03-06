from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')
    date = models.DateField()
    tags = models.CharField(max_length=20)

    def __str__(self):
        return self.title
