from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=25)


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Produtos(models.Model):
    descricao = models.CharField(max_length=250)
    quantidade_estoque = models.IntegerField(default=0)
    valor = models.FloatField()
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)


class Clientes(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cpf = models.IntegerField(unique=True)
    cep = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)




