from app import db
from app.models import Pedido, ItemPedido, FatoVendas
import json
from datetime import datetime

class ETLAgent:
    @staticmethod
    def processar_pedido(pedido_id):
        """
        Processa um pedido e carrega os dados no Data Warehouse
        """
        try:
            # Extrair dados do pedido
            pedido = Pedido.query.get(pedido_id)
            if not pedido:
                raise Exception("Pedido não encontrado")

            # Calcular valor total e quantidade de itens
            valor_total = 0
            quantidade_itens = 0
            itens_detalhados = []

            for item in pedido.itens:
                valor_total += item.preco_unitario * item.quantidade
                quantidade_itens += item.quantidade
                itens_detalhados.append({
                    'produto_id': item.produto_id,
                    'quantidade': item.quantidade,
                    'preco_unitario': item.preco_unitario,
                    'subtotal': item.preco_unitario * item.quantidade
                })

            # Preparar dados para o DW
            dados_pedido = {
                'itens': itens_detalhados,
                'status': pedido.status,
                'data_pedido': pedido.data.isoformat()
            }

            # Criar registro no DW
            fato_vendas = FatoVendas(
                pedido_id=pedido.id,
                usuario_id=pedido.usuario_id,
                data_pedido=pedido.data,
                valor_total=valor_total,
                quantidade_itens=quantidade_itens,
                dados_pedido=json.dumps(dados_pedido)
            )

            # Salvar no DW
            db.session.add(fato_vendas)
            db.session.commit()

            return True, "Dados processados com sucesso"

        except Exception as e:
            db.session.rollback()
            return False, f"Erro ao processar pedido: {str(e)}" 