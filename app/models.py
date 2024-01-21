from django.db import models

# Create your models here.
class Preview(models.Model):
    title = models.CharField(max_length=512)
    img = models.CharField(max_length=512)
