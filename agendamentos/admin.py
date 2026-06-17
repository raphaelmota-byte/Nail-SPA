from django.contrib import admin
from .models import Cliente , Servico , Agendamento , ConfiguracaoSite

admin.site.register(Cliente)
admin.site.register(Servico)
admin.site.register(Agendamento)
admin.site.register(ConfiguracaoSite)


# Register your models here.
