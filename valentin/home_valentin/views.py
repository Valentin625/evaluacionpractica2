from django.shortcuts import render

def inicio(request):
    generos = [
        {"nombre": "Acción", "descripcion": "Películas llenas de adrenalina"},
        {"nombre": "Comedia", "descripcion": "Películas para reír"}
    ]
    return render(request, "inicio.html", {"generos": generos})

def accion(request):
    peliculas = [
        {"nombre": "Mad Max", "edad": "16+", "imagen": "madmax.webp"},
        {"nombre": "John Wick", "edad": "18+", "imagen": "john-wick-franchise-poster.avif"}
    ]
    return render(request, "accion.html", {"peliculas": peliculas})

def comedia(request):
    peliculas = [
        {"nombre": "Superbad", "edad": "16+", "imagen": "superbad.jpg"},
        {"nombre": "The Mask", "edad": "12+", "imagen": "themask.webp"}
    ]
    return render(request, "comedia.html", {"peliculas": peliculas})
