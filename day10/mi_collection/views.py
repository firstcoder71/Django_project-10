from django.shortcuts import render
from . models import PhoneCollection
from . forms import Phone_Userinfo

# Create your views here.
def phone_data(request):
    phon = PhoneCollection.objects.all()
    return render(request,'migrate/phone.html',{'PHONE':phon})

def phon_info(request):
    frm = Phone_Userinfo
    request render(request,'')

