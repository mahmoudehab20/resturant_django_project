from django.db import models

class MainDish(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(max_length=6)
    stock = models.IntegerField()
    image=models.ImageField(upload_to='food/',null=True,blank=True)

    def __str__(self):
        return self.title
    
    def get_image_url(self):
        return f"/media/{self.image}"

class appetizers(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(max_length=6)
    stock = models.IntegerField()
    image=models.ImageField(upload_to='appetizers/',null=True,blank=True)

    def __str__(self):
        return self.title
    
    def get_image_url(self):
        return f"/media/{self.image}"

    
class souces(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(max_length=6)
    stock = models.IntegerField()
    image=models.ImageField(upload_to='souce/',null=True,blank=True)

    def __str__(self):
        return self.title

    def get_image_url(self):
        return f"/media/{self.image}"
