from .models import Clientes, Produtos


def get_produto(id):  # Pegar id do produto
    try:
        return Produtos.objects.get(id=id)
        
    except Produtos.DoesNotExist:
        return None


def get_cliente(id):  # Pegar id do cliente
        try:
           return Clientes.objects.get(id=id)
        
        except Clientes.DoesNotExist:
            return None
    