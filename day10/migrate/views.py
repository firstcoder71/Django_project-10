from django.shortcuts import render
from . models import Student_Info

# Create your views here.
def Profile_Table(request):
    pro_table = Student_Info.objects.all()
    return render(request,'migrate/index.html',{'empd':pro_table})
