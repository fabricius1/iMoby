from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Cidade, Imovel


@login_required(login_url='/auth/login')
def home(request):
    preco_minimo = request.GET.get('preco_minimo')
    preco_maximo = request.GET.get('preco_maximo')
    cidade = request.GET.get('cidade')
    tipo = request.GET.getlist('tipo')    
    cidades = Cidade.objects.all()
    
    if preco_minimo or preco_maximo or cidade or tipo:
        
        if not preco_minimo:
            preco_minimo = 0
        if not preco_maximo:
            preco_maximo = 999999999
        if not tipo:
            tipo = ['A', 'C']
        
        imoveis = (Imovel.objects
                     .filter(valor__gte=preco_minimo)
                     .filter(valor__lte=preco_maximo)
                     .filter(tipo_imovel__in=tipo)
                     .filter(cidade=cidade)
                  )
    else:
        imoveis = Imovel.objects.all()
   
    return render(request, 'home.html', {'imoveis': imoveis, 'cidades': cidades})


def imovel(request, id):
    imovel = get_object_or_404(Imovel, id=id)
    sugestoes = Imovel.objects.filter(cidade=imovel.cidade).exclude(id=id)[:2]
    return render(request, 'imovel.html', {'imovel': imovel, 'sugestoes': sugestoes, 'id': id})