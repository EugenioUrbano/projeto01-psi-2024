from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def jogadores(request):
    jogadores = [
        {"Nome": "Diego Roncaglio", "Idade": "36 anos", "Posicao": "Goleiro", "Naturalidade": "Blumenau - SC", "foto" : "jogador_01.jpg"},
        {"Nome": "João Victor (Neguinho)", "Idade": "24 anos", "Posicao": "Fixo", "Naturalidade": "São Paulo - SP", "foto" : "jogador_02.jpg"},
        {"Nome": "Fabrício Bastezini (Gadeia)", "Idade": "36 anos", "Posicao": "Fixo", "Naturalidade": "São Lourenço do Oeste - SC", "foto" : "jogador_03.jpg"},
        {"Nome": "Marlon Araújo", "Idade": "36 anos", "Posicao": "Fixo", "Naturalidade": "Salvador - BH", "foto" : "jogador_04.jpg"},
        {"Nome": "Felipe Valério", "Idade": "31 anos", "Posicao": "Fixo", "Naturalidade": "Suzano - SP", "foto" : "jogador_05.jpg"},
        {"Nome": "Arthur Guilherme", "Idade": "30 anos", "Posicao": "Ala", "Naturalidade": "Uberlandia - MG", "foto" : "jogador_06.jpg"},
        {"Nome": "Marcênio Ribeiro", "Idade": "36 anos", "Posicao": "Ala", "Naturalidade": "Campo Grande - MS", "foto" : "jogador_07.jpg"},
        {"Nome": "Diego Nunes", "Idade": "29 anos", "Posicao": "Ala", "Naturalidade": "Guarulhos - SP", "foto" : "jogador_08.jpg"},
        {"Nome": "Rafael dos Santos", "Idade": "33 anos", "Posicao": "Pivô", "Naturalidade": "São Bernardo do Campo - SP", "foto" : "jogador_09.jpg"},
        {"Nome": "Jean Pierre", "Idade": "32 anos", "Posicao": "Pivô", "Naturalidade": "Chapeco - SC", "foto" : "jogador_10.jpg"},
        {"Nome": "Vinicius Nunes", "Idade": "29 anos", "Posicao": "Goleiro", "Naturalidade": "São Vicente - SP", "foto" : "jogador_11.jpg"},
    ]
    context = {
        "jogadores": jogadores,
    }
    return render(request, "jogadores.html", context)

def sobre(request):
    return render(request, "sobre.html")