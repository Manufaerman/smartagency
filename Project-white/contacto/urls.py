from django.urls import path
from contacto import views



urlpatterns = [
    path("",views.store, name="contacto"),
    
    
    ]