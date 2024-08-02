from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def jogadores(request):
    jogadores = [
        {"Nome": "Lionel Messi", "idade": "32"}
    ]
    context = {
        "atletas": jogadores,
    }
    return render(request, "sobre.html"),

def sobre(request):
    return render(request, "sobre.html")