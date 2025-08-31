from django.shortcuts import render
from django.http import HttpResponse

def primeiraPagina(request):
    return HttpResponse("Fabricio Batista de Araujo - 01706468")

