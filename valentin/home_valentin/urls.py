from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("accion/", views.accion, name="accion"),
    path("comedia/", views.comedia, name="comedia"),  
]
