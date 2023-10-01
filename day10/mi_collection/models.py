from django.db import models

# Create your models here.
class PhoneCollection(models.Model):
    Phone_name = models.CharField(max_length=20)
    Brand_name = models.CharField(max_length=20)
    Realesed_date = models.CharField(max_length=20)
    Price = models.CharField(max_length=20)
