from django import forms

class Phone_Userinfo(forms.Form):
    first_name = forms.CharField()
    Username = forms.CharField()
    Email = forms.CharField(required=True)
    Password = forms.CharField(widget=forms.PasswordInput())
    Address = forms.CharField(widget= forms.Textarea())

    
