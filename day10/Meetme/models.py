from django.db import models

# Create your models here.
class User_info(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=40)
    user_id = models.CharField(max_length=20)
    user_phonenumber = models.CharField(max_length=14)
    user_address = models.CharField(max_length=100)
