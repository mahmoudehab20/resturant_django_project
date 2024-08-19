from django.db import models

class MainDish(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(max_length=6)
    stock = models.IntegerField()

    def __str__(self):
        return self.title

class appetizers(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(max_length=6)
    stock = models.IntegerField()

    def __str__(self):
        return self.title
    
class souces(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(max_length=6)
    stock = models.IntegerField()

    def __str__(self):
        return self.title
