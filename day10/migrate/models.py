from django.db import models

# Create your models here.
class Student_Info(models.Model):
    employe_name = models.CharField(max_length=30)
    employe_number = models.IntegerField()
    employe_email = models.CharField(max_length=40)
    employe_id = models.IntegerField()
    employe_position = models.CharField(max_length=30)