from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='listings'),
    path('adverticement', views.listing, name='adverticement'),
]
