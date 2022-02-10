from pyexpat import model
from django.db import models
from django.shortcuts import redirect

# Create your models here.

class Joe(models.Model):
    name = models.CharField(max_length=200)
    buyer_phrase = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="pics/", null=True, blank=True)

    def __str__(self):
        return self.name
        