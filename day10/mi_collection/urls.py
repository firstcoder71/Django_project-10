from django.urls import path
from . import views


urlpatterns = [
    path('phon/',views.phone_data),
]
