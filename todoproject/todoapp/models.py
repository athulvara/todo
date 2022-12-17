

from django.db import models

# Create your models here.

class Task(models.Model):
    name=models.CharField(max_length=250)
    priority=models.IntegerField()
    #date=models.DateField('date', blank=True, null=True, default="2000-02-22")

    def __str__(self):
        return self.name