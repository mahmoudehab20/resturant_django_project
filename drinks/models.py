from django.db import models

# Create your models here.
class drinks(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.FloatField(max_length=6)
    stock=models.IntegerField()

    def __str__(self):
        return self.title
