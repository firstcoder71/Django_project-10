from django.contrib import admin
from .models import Sell_Info
# Register your models here.
class TrafficAdmin(admin.ModelAdmin):
    list_display = ('traffic_name','traffic_email','phone_number','transaction_id','traffic_address')

admin.site.register(Sell_Info,TrafficAdmin)
