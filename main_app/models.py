from django.db import models



class Finch(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    habitat = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    nesting = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

