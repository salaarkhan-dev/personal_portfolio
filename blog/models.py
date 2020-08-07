from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog/images/')
    tags = models.CharField(max_length=20)

    def __str__(self):
        return self.title
