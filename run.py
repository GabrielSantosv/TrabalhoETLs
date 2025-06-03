from app import app, client, produtos
from app.models import Produto
import traceback

def init_db():
    """Inicializa os bancos de dados e cria algumas tabelas de exemplo"""
    try:
        print("Tentando conectar ao MongoDB...")
        # Testar conexão com MongoDB
        client.admin.command('ping')
        print("Conexão com MongoDB Atlas estabelecida com sucesso!")
        
        # Verificar se já existem produtos
        if produtos.count_documents({}) == 0:
            print("Criando produtos de exemplo...")
            # Criar alguns produtos de exemplo
            produtos_exemplo = [
                Produto(nome='Smartphone XYZ', preco=1999.99, estoque=50),
                Produto(nome='Notebook ABC', preco=3999.99, estoque=30),
                Produto(nome='Tablet 123', preco=999.99, estoque=100)
            ]
            # Inserir produtos no MongoDB
            for produto in produtos_exemplo:
                produtos.insert_one(produto.to_dict())
            print("Produtos de exemplo criados com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar com MongoDB: {str(e)}")
        print("Detalhes do erro:")
        print(traceback.format_exc())
        raise e

if __name__ == '__main__':
    try:
        init_db()
        print("Iniciando servidor Flask...")
        app.run(debug=True)
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {str(e)}")
        print("Detalhes do erro:")
        print(traceback.format_exc()) 