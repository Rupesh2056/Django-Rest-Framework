from django.db import models

# Create your models here.
class Band(models.Model):
    Title = models.CharField(max_length=50)
    Genre = models.CharField(max_length=50)
    Established = models.DateField(null=True,blank=True)
    Albums =models.IntegerField()

    def __str__(self):
        return self.Title