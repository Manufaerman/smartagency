from django.urls import path
from whitehouse.views import Booking, RentFlatsByUsersList
from whitehouse import views
from django.conf import settings


urlpatterns = [
    path("",views.home, name="home"),
    path("flat/<categoria_id>/",views.store, name="flat"),
    path("description/<categoria_id>/",views.description, name="description"),
    path('booking/<categoria_id>', Booking.as_view(), name='Booking'),
    path('rent_flats/', RentFlatsByUsersList.as_view(), name='my_Booking')


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)