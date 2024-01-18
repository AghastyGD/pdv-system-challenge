from django.db import models
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, senha=None, **extra_fields):
        if not email:
            raise ValueError('O campo de email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, **extra_fields)
        user.senha = make_password(senha)
        user.save(using=self._db)

        return user

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128, default=None)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.senha = make_password(self.senha)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.senha)
    
    @property
    def is_anonymous(self):
        return False
    
    @property
    def is_authenticated(self):
        return True


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

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




