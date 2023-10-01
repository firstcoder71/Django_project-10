from django.contrib import admin
from . models import PhoneCollection

# Register your models here.
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('Phone_name','Brand_name','Realesed_date','Price')
    

admin.site.register(PhoneCollection,PhoneAdmin)
