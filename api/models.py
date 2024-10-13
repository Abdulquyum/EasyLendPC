from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Laptop(models.Model):
    owner = models.CharField(max_length=225, default="EasyLendPC")
    name = models.CharField(max_length=220)
    description = models.TextField(max_length=225)
    status = models.CharField(max_length=225)
    image = models.ImageField(null=False, blank=True, upload_to="images/")


    def __str__(self):
        return f"{self.name} {self.owner}"

    def get_absolute_url(self):
        # return reverse('laptop-details', args=(str(self.id)))
        return reverse('display')



class LendOutPc(models.Model):
    pc_owner = models.CharField(max_length=225)
    pc_name = models.CharField(max_length=225)
    pc_description = models.TextField(max_length=225)
    pc_status = models.CharField(max_length=225)
    phone_number = models.IntegerField()
    image = models.ImageField(null=False, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.pc_name} {self.pc_owner}"

    def get_absolute_url(self):
        return reverse('non_company_pc')
