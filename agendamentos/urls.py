from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # o name é usado no html, permitindo trocar o path sem
    # quebrar o html , o views.listar_servicos é simplesmente um from . views import lista_servicos
]