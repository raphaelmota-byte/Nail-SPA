from django.shortcuts import render
from .models import Servico , ConfiguracaoSite

def home(request):
    servicos = Servico.objects.filter(ativo=True)
    config = ConfiguracaoSite.objects.first()
    
    
    return render(request , "agendamentos/home.html" , {
        "servicos" : servicos ,
        "config" : config
    })

