from django.db import models

# Create your models here.
class Midia(models.Model):
    nome = models.CharField(max_length=45)

class Local(models.Model):
     cidade = models.CharField(max_length=45)
     estado = models.CharField(max_length=45)
     regiao = models.CharField(max_length=45)
     pais   = models.CharField(max_length=45)

class Indicador(models.Model):
    data = models.DateTimeField('date published')
    seguidores = models.IntegerField(default=0)
    visualizacoes = models.IntegerField(default=0)
    comentarios = models.IntegerField(default=0)
    compartilhamentos = models.IntegerField(default=0)
    midia = models.ForeignKey(Midia, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)