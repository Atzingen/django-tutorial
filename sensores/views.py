from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return render(request, 'home.html', {'lista_numeros': lista_numeros})

def about(request):
    return HttpResponse("<h1>About page</h1>")

def sensor_input(request, valor):
    return HttpResponse(f"<h1>Valor do sensor: {valor}</h1>")