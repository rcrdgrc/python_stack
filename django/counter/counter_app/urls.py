from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('plus2', views.plus2),
    path('destroy_session', views.destroy_session),
]