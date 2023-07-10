from django.db import models

# Create your models here.
class Cakes(models.Model):
    name=models.CharField(max_length=250)
    
    flavour=models.CharField(max_length=250)
    price=models.PositiveIntegerField()
    shape=models.CharField(max_length=200)
    weight=models.CharField(max_length=200)
    layer=models.PositiveIntegerField()
    description=models.CharField(max_length=2550)
    profile=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.name