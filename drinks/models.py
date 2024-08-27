from django.db import models
from django.contrib import messages
# Create your models here.
class drinks(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.FloatField(max_length=6)
    stock=models.IntegerField()
    image=models.ImageField(upload_to='drinks/',null=True,blank=True)

    def __str__(self):
        return self.title
    
    def get_image_url(self):
        return f"/media/{self.image}"
