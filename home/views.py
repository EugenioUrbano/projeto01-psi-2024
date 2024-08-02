from django.shortcuts import render

def home(request):
    return render(request, 'home/templates/index.html')

def home(request):
    return render(request, 'templates/jogadores.html')

def home(request):
    return render(request, 'home/templates/sobre.html')
