
from django.urls import path
from django.urls.conf import include, include
from django.conf import settings
from accounts import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path("login/ [name='login']", include('django.contrib.auth.urls')),
    path("accounts/ logout/ [name='logout']", include('django.contrib.auth.urls')),
    path("accounts/ password_change/ [name='password_change']", include('django.contrib.auth.urls')),
    path("accounts/ password_change/done/ [name='password_change_done']", include('django.contrib.auth.urls')),
    path("accounts/ password_reset/ [name='password_reset']", include('django.contrib.auth.urls')),
    path("accounts/ password_reset/done/ [name='password_reset_done']", include('django.contrib.auth.urls')),
    path("accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']", include('django.contrib.auth.urls')),
    path("accounts/ reset/done/ [name='password_reset_complete']", include('django.contrib.auth.urls')),
    





]






    