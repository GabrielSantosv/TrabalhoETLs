from flask import jsonify, request
from app import app, usuarios, produtos, pedidos, fato_vendas
from app.models import Usuario, Produto, Pedido, FatoVendas
from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId
import json

@app.route('/criarConta', methods=['POST'])
def criar_conta():
    try:
        dados = request.get_json()
        
        # Validar dados
        if not all(k in dados for k in ['nome', 'email', 'senha']):
            return jsonify({'erro': 'Dados incompletos'}), 400

        # Verificar se email já existe
        if usuarios.find_one({'email': dados['email']}):
            return jsonify({'erro': 'Email já cadastrado'}), 400

        # Criar usuário
        usuario = Usuario(
            nome=dados['nome'],
            email=dados['email'],
            senha=generate_password_hash(dados['senha'])
        )

        # Inserir no MongoDB
        result = usuarios.insert_one(usuario.to_dict())

        return jsonify({
            'mensagem': 'Conta criada com sucesso',
            'usuario_id': str(result.inserted_id)
        }), 201

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    try:
        dados = request.get_json()
        
        # Validar dados
        if not all(k in dados for k in ['email', 'senha']):
            return jsonify({'erro': 'Dados incompletos'}), 400

        # Buscar usuário
        usuario = usuarios.find_one({'email': dados['email']})
        if not usuario or not check_password_hash(usuario['senha'], dados['senha']):
            return jsonify({'erro': 'Email ou senha inválidos'}), 401

        return jsonify({
            'mensagem': 'Login realizado com sucesso',
            'usuario_id': str(usuario['_id'])
        }), 200

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/faturarPedido', methods=['POST'])
def faturar_pedido():
    try:
        dados = request.get_json()
        
        # Validar dados
        if not all(k in dados for k in ['usuario_id', 'produtos']):
            return jsonify({'erro': 'Dados incompletos'}), 400

        # Preparar itens do pedido
        itens_pedido = []
        for item in dados['produtos']:
            produto = produtos.find_one({'_id': ObjectId(item['id'])})
            if not produto:
                raise Exception(f"Produto {item['id']} não encontrado")
            
            if produto['estoque'] < item['quantidade']:
                raise Exception(f"Estoque insuficiente para o produto {produto['nome']}")

            # Atualizar estoque
            produtos.update_one(
                {'_id': ObjectId(item['id'])},
                {'$inc': {'estoque': -item['quantidade']}}
            )

            itens_pedido.append({
                'produto_id': str(produto['_id']),
                'quantidade': item['quantidade'],
                'preco_unitario': produto['preco']
            })

        # Criar pedido
        pedido = Pedido(
            usuario_id=ObjectId(dados['usuario_id']),
            itens=itens_pedido
        )
        
        # Inserir pedido
        result = pedidos.insert_one(pedido.to_dict())
        
        # Criar fato de vendas
        fato = FatoVendas(pedido)
        fato_vendas.insert_one(fato.to_dict())

        return jsonify({
            'mensagem': 'Pedido faturado com sucesso',
            'pedido_id': str(result.inserted_id)
        }), 201

    except Exception as e:
        return jsonify({'erro': str(e)}), 500 