from django.db import models

# Create your models here.
class Rakuten(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    descripton = models.TextField
    material = models.CharField(max_length=100)
    