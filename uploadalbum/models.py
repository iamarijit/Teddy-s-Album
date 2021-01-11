from django.db import models

# Create your models here.
class Photo(models.Model):
    name = models.TextField(blank=True)
    image = models.ImageField(upload_to="imageuploads")
