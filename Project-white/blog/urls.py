from django.urls import path
from blog import views
from django.conf import settings



urlpatterns = [
    path("",views.blogging, name="blog"),
    path("categoria/<categoria_id>/",views.categoria, name="categoria"),
    
    

]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)