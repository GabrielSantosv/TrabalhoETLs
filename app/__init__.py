from flask import Flask
from pymongo import MongoClient
import os

# Inicialização do Flask
app = Flask(__name__)

# Configuração do MongoDB Atlas
client = MongoClient('mongodb+srv://mongo:mongo@trabalhoetls.i9fejdf.mongodb.net/')
db_transactional = client['ecommerce']
db_warehouse = client['ecommerce_dw']

# Coleções do banco transacional
usuarios = db_transactional['usuarios']
produtos = db_transactional['produtos']
pedidos = db_transactional['pedidos']

# Coleções do Data Warehouse
fato_vendas = db_warehouse['fato_vendas']

# Garantir que os diretórios existam
os.makedirs('../data', exist_ok=True)

# Importar rotas
from app import routes 