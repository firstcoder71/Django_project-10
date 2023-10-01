from django.contrib import admin
from.models import User_info

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name','user_email','user_id','user_phonenumber','user_address')

admin.site.register(User_info,UserAdmin)
