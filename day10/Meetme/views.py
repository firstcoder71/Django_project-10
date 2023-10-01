from django.shortcuts import render
from.models import User_info

# Create your views here.
def userin(request):
    user_var = User_info.objects.all()
    return render(request,'migrate/userinfo.html',{'USERINFO':user_var})
