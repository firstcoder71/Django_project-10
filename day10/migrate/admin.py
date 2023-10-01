from django.contrib import admin
from . models import Student_Info


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('employe_name','employe_number','employe_email','employe_position')

admin.site.register(Student_Info, StudentAdmin)
