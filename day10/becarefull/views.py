from django.shortcuts import render
from becarefull.models import *

# Create your views here.
def sells(request):
    sells_in = Sell_Info.objects.all()
    return render(request,'migrate/sellsinfo.html',{'sellde':sells_in})
