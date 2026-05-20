import asyncio
import httpx

# RPC Público descentralizado (Sem necessidade de cadastro ou tokens)
RPC_NODE_URL = "https://base.org"

async def escutar_blockchain():
    # Inicializa cliente HTTP/2 para alta performance e conexões persistentes
    async with httpx.AsyncClient(http2=True) as client:
        print("🔌 Conexão estabelecida com a infraestrutura da rede Base. Escutando blocos...")
        
        ultimo_bloco = 0
        
        while True:
            try:
                # 1. Busca o número do bloco mais recente minerado na rede
                payload_bloco = {
                    "jsonrpc": "2.0",
                    "method": "eth_blockNumber",
                    "params": [],
                    "id": 1
                }
                response = await client.post(RPC_NODE_URL, json=payload_bloco)
                bloco_hex = response.json()['result']
                bloco_atual = int(bloco_hex, 16)
                
                # 2. Se um novo bloco surgiu, mineramos as transações brutas de dentro dele
                if bloco_atual > ultimo_bloco:
                    if ultimo_bloco == 0:
                        ultimo_bloco = bloco_atual - 1
                        
                    for num_bloco in range(ultimo_bloco + 1, bloco_atual + 1):
                        payload_transacoes = {
                            "jsonrpc": "2.0",
                            "method": "eth_getBlockByNumber",
                            "params": [hex(num_bloco), True], # True baixa o corpo completo das transações
                            "id": 2
                        }
                        resp_tx = await client.post(RPC_NODE_URL, json=payload_transacoes)
                        dados_bloco = resp_tx.json().get('result')
                        
                        if dados_bloco and dados_bloco.get('transactions'):
                            lista_tx = dados_bloco['transactions']
                            print(f"📦 BLOCO PROVADO | Número: {num_bloco} | {len(lista_tx)} transações processadas.")
                            
                            for tx in lista_tx:
                                # Converte o valor bruto de Wei para ETH
                                valor_wei = int(tx.get('value', '0x0'), 16)
                                valor_eth = valor_wei / 10**18
                                
                                # FILTRO CRÍTICO: Detecta transferências acima de 10 ETH
                                if valor_eth > 10.0:
                                    hash_tx = tx.get('hash')
                                    print(f"🚨 MOVIMENTAÇÃO DE BALEIA DETECTADA | {valor_eth:.2f} ETH | Hash: {hash_tx[:12]}...")
                                    
                    ultimo_bloco = bloco_atual
                    
            except Exception as erro:
                print(f"❌ Falha temporária na requisição RPC: {erro}")
                
            # Intervalo de 2 segundos (tempo médio de criação de blocos na L2) para evitar spam
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(escutar_blockchain())
