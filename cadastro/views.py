from django.shortcuts import render, redirect

def paginaExterna(request):
    return render(request, 'cadastro/pagina.html')

def barbearia(request):
    return render(request, 'cadastro/barbearia.html')

def sair(request):
    return redirect('externa')  
