from django.db import models

# Create your models here.
class Preview(models.Model):
    title = models.CharField()
    img = models.CharField()
