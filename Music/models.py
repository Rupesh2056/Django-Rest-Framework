from django.db import models

# Create your models here.

class Album(models.Model):
    Title = models.CharField(max_length=50)
    Artist = models.CharField(max_length=50)
    Tracks = models.IntegerField()
    Length = models.FloatField()
    Rating = models.FloatField(null=True)

    def __str__(self):
        return self.Title

