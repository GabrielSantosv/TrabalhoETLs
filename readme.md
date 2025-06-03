# Sistema ETL para E-commerce

Este projeto implementa um sistema de backend para e-commerce com agentes ETL (Extract, Transform, Load) para popular um Data Warehouse.

## Descrição

O sistema consiste em:
- Backend de e-commerce com rotas REST
- Banco de dados transacional (SQLite)
- Data Warehouse (SQLite)
- Agentes ETL para sincronização de dados

## Requisitos

- Python 3.8+
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Estrutura do Projeto

```
.
├── app/
│   ├── __init__.py
│   ├── models.py          # Modelos do banco de dados
│   ├── etl_agents.py      # Agentes ETL
│   └── routes.py          # Rotas da API
├── data/
│   ├── transactional.db   # Banco de dados transacional
│   └── warehouse.db       # Data Warehouse
├── requirements.txt
└── run.py                 # Arquivo principal
```

## Funcionalidades

### Rotas da API

- `POST /criarConta`: Registro de novos usuários
- `POST /login`: Autenticação de usuários
- `POST /faturarPedido`: Processamento de pedidos

### Agentes ETL

- Extração automática de dados após operações transacionais
- Transformação dos dados para o formato do DW
- Carregamento no Data Warehouse

## Como Executar

1. Inicie o servidor:
```bash
python run.py
```

2. O servidor estará disponível em `http://localhost:5000`

## Exemplos de Uso

### Criar Conta
```bash
curl -X POST http://localhost:5000/criarConta \
  -H "Content-Type: application/json" \
  -d '{"nome": "João Silva", "email": "joao@email.com", "senha": "123456"}'
```

### Login
```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"email": "joao@email.com", "senha": "123456"}'
```

### Faturar Pedido
```bash
curl -X POST http://localhost:5000/faturarPedido \
  -H "Content-Type: application/json" \
  -d '{"usuario_id": 1, "produtos": [{"id": 1, "quantidade": 2}]}'
```
