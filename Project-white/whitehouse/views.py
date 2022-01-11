from django.db.models.base import Model
from django.forms.forms import Form
from django.http import request
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.views import generic
from .models import Vivienda, Categorias, reservas
import uuid
from .forms import AvailabilityForm
from whitehouse.booking_functions.availability import check_availability
from django.views.generic import FormView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    articulo = Vivienda.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request,"whitehouse/home.html",{"articulo":articulo, 'num_visits':num_visits})


def store(request, categoria_id):
    categorias = Categorias.objects.get(id=categoria_id)
    vivienda = reservas.objects.all()
    return render(request,"whitehouse/flat.html",{'categorias':categorias,'vivienda':vivienda})

def description(request, categoria_id,):
    vivienda = get_object_or_404(Vivienda,id=categoria_id)
    books = reservas.objects.filter(vivienda=vivienda)
    books1= books[0].__dict__
    if(request.POST):
        form=request.POST.dict()
    
        booking = reservas.objects.create(
        user = request.user,
        vivienda = vivienda,
        numero = 1,
        fecha_entrada = form['check_in'],
        fecha_salida = form['check_out']
        )
        booking.save
                
        return HttpResponse(booking)
        

    else:    
        form = AvailabilityForm()
    
    return render(request,"whitehouse/description.html",{'vivienda':vivienda, 'form':form, 'books1':books1})


class Booking(ListView):
    model = reservas

    def get_queryset(self):
        return reservas.objects.filter(vivienda=self.request.categoria_id)
    

class RentFlatsByUsersList(LoginRequiredMixin,generic.ListView):
    model=reservas
    template_name = 'whitehouse/vivienda_list_rented_user.html'

    def get_queryset(self):
        return reservas.objects.filter(user=self.request.user).filter(status__exact='o').order_by('fecha_salida')
    

    


        




MEDIA_SERVER = 'http://127.0.0.1:8000/media/'
 
 
class ImageTool:
    @staticmethod
    def get_new_random_file_name(file_name):
        find_type = False
        for c in file_name:
            if c == '.':
                find_type = True
        if find_type:
            type = file_name.split('.')[-1]
            return str(uuid.uuid1()) + '.' + type
        else:
            return str(uuid.uuid1())
 
 






