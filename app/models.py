from datetime import datetime
from bson import ObjectId
import json

# Estruturas de dados para MongoDB
class Usuario:
    def __init__(self, nome, email, senha):
        self._id = ObjectId()
        self.nome = nome
        self.email = email
        self.senha = senha
        self.data_criacao = datetime.utcnow()

    def to_dict(self):
        return {
            '_id': self._id,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha,
            'data_criacao': self.data_criacao
        }

class Produto:
    def __init__(self, nome, preco, estoque):
        self._id = ObjectId()
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def to_dict(self):
        return {
            '_id': self._id,
            'nome': self.nome,
            'preco': self.preco,
            'estoque': self.estoque
        }

class Pedido:
    def __init__(self, usuario_id, itens):
        self._id = ObjectId()
        self.usuario_id = usuario_id
        self.data = datetime.utcnow()
        self.status = 'faturado'
        self.itens = itens  # Lista de itens do pedido
        self.valor_total = sum(item['quantidade'] * item['preco_unitario'] for item in itens)

    def to_dict(self):
        return {
            '_id': self._id,
            'usuario_id': self.usuario_id,
            'data': self.data,
            'status': self.status,
            'itens': self.itens,
            'valor_total': self.valor_total
        }

# Modelo para o Data Warehouse
class FatoVendas:
    def __init__(self, pedido):
        self._id = ObjectId()
        self.pedido_id = pedido._id
        self.usuario_id = pedido.usuario_id
        self.data_pedido = pedido.data
        self.valor_total = pedido.valor_total
        self.quantidade_itens = sum(item['quantidade'] for item in pedido.itens)
        self.dados_pedido = {
            'itens': pedido.itens,
            'status': pedido.status,
            'data_pedido': pedido.data.isoformat()
        }

    def to_dict(self):
        return {
            '_id': self._id,
            'pedido_id': self.pedido_id,
            'usuario_id': self.usuario_id,
            'data_pedido': self.data_pedido,
            'valor_total': self.valor_total,
            'quantidade_itens': self.quantidade_itens,
            'dados_pedido': self.dados_pedido
        } 