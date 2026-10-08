from django.urls import path, include

urlpatterns = [
    path("", include("home_valentin.urls")),  # conecta la app
]
