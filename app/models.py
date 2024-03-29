from django.db import models
from django.contrib.postgres.search import SearchVectorField

# Create your models here.
class Preview(models.Model):
    title = models.CharField(max_length=512)
    title_tsvector = SearchVectorField(null=True)
    img = models.CharField(max_length=512)
    kind = models.CharField(max_length=64, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['kind'])
        ]


