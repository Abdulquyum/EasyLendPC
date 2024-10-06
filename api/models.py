from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Laptop(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    status = models.CharField(max_length=225)
    image = models.ImageField(null=True, blank=True, upload_to="images/")


    def __str__(self):
        return self.description