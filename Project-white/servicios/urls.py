from django.urls import path
from servicios import views
from django.conf import settings


urlpatterns = [
    path("",views.servicios, name="servicios"),
    path("<servicio_nombre>/",views.animal, name="servicios"),
    
    
    

]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)