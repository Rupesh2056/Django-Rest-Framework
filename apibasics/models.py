from django.db import models

# Create your models here.

class Article(models.Model):
    Title = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    Date = models.DateTimeField(auto_now=True)
    Email= models.EmailField()

    def __str__(self):
        return self.Title
