from django.db import models

# Create your models here.
class Sell_Info (models.Model):
    traffic_name = models.CharField(max_length=30)
    traffic_email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=120)
    transaction_id = models.IntegerField()
    traffic_address = models.CharField(max_length=100)
