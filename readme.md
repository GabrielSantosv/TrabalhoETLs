# 🛒 Sistema ETL para E-commerce

Este projeto implementa um sistema backend para e-commerce com agentes ETL que integram um banco de dados transacional com um Data Warehouse, permitindo análises em tempo real.

## 📦 Funcionalidades

✅ Backend com rotas REST  
✅ Banco de dados transacional (MongoDB)  
✅ Data Warehouse (MongoDB)  
✅ Agentes ETL automáticos  
✅ Operações de criar conta, login e faturamento de pedidos

---

## ⚙️ Como funciona?

1. **Usuário realiza ações via API** (`/criarConta`, `/login`, `/faturarPedido`)
2. **Os dados são salvos no banco transacional**
3. **Agentes ETL entram em ação automaticamente:**
   - **Extraem** dados do banco transacional
   - **Transformam** para o formato correto
   - **Carregam** no Data Warehouse

---

## 🚀 Instalação

```bash
# Clone o repositório
git clone <repo-url>
cd TrabalhoETLs-main

# Crie um ambiente virtual
python -m venv venv
# Ative o ambiente:
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

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

  Invoke-WebRequest -Method POST -Uri http://localhost:5000/criarConta -Headers @{"Content-Type" = "application/json"} -Body ([System.Text.Encoding]::UTF8.GetBytes('{"nome": "Nome do Usuário", "email": "email.unico@example.com", "senha": "suaSenha"}'))
```

### Login
```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"email": "joao@email.com", "senha": "123456"}'
  
  Invoke-WebRequest -Method POST -Uri http://localhost:5000/login -Headers @{"Content-Type" = "application/json"} -Body ([System.Text.Encoding]::UTF8.GetBytes('{"email": "email.cadastrado@example.com", "senha": "senhaDoUsuario"}'))
```

### Faturar Pedido
```bash
curl -X POST http://localhost:5000/faturarPedido \
  -H "Content-Type: application/json" \
  -d '{"usuario_id": 1, "produtos": [{"id": 1, "quantidade": 2}]}'

  Invoke-WebRequest -Method POST -Uri http://localhost:5000/faturarPedido -Headers @{"Content-Type" = "application/json"} -Body ([System.Text.Encoding]::UTF8.GetBytes('{"usuario_id": "COLOQUE_AQUI_O_ID_REAL_DO_USUARIO", "produtos": [{"id": "COLOQUE_AQUI_O_ID_REAL_DO_PRODUTO", "quantidade": 2}]}'))
```

