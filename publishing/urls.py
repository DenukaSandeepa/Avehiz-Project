from django.urls import path
from . import views

urlpatterns = [
    path('', views.posting, name='publishing'),
    path('<int:publish_id>', views.detail, name='details'),
]
