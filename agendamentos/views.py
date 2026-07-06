from django.shortcuts import render
from .models import Servico , ConfiguracaoSite

def home(request):
    servicos = Servico.objects.filter(ativo=True)
    config = ConfiguracaoSite.objects.first()
    
    dicionario_galeria_alt = {
    "agendamentos/img/galeria/alongamento.jpg": "alongamento",
    "agendamentos/img/galeria/pe.avif": "pe",
    "agendamentos/img/galeria/ambiente_sofisticado.png": "ambiente sofisticado",
    "agendamentos/img/galeria/bioseguranca.png": "biosegurança",
    "agendamentos/img/galeria/foto_servico_manicure.jfif": "manicure",
    "agendamentos/img/galeria/foto_unha_azul.webp": "unha azul",
    "agendamentos/img/galeria/produtos_premium.jfif": "produtos premium"
        
    }
    
    
    return render(request , "agendamentos/home.html" , {
        "servicos" : servicos ,
        "config" : config ,
        "dic_galeria_alt" : dicionario_galeria_alt
    })

