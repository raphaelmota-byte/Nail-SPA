from tokenize import blank_re
from django.db import models 
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.user.get_full_name() or self.user.username
    
class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    duracao = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=8 , decimal_places=2)
    ativo = models.BooleanField(default=True) 
    foto = models.ImageField(upload_to='servicos/', blank=True , null=True)
    
    def __str__(self):
        return self.nome
    
class Agendamento(models.Model):
    STATUS_CHOICES = [  
                       
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
        ('concluido', 'Concluído'),
        
                    ]
    
    
    
    cliente = models.ForeignKey(Cliente , on_delete=models.PROTECT)
    servico = models.ForeignKey(Servico , on_delete=models.PROTECT)
    data = models.DateField()
    horario = models.TimeField()
    status = models.CharField( max_length=20, choices=STATUS_CHOICES, default='pendente')
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.cliente} - {self.servico} - {self.data}"
    
class ConfiguracaoSite(models.Model):
    foto_inicio = models.ImageField(blank=True , null=True , upload_to="inicio/")
    ativacao = models.BooleanField(default=True)
    
    def __str__(self):
        return self.foto_inicio.name