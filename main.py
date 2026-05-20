import asyncio
import httpx

# Endpoint RPC público e estável da rede Base (mantido pela Ankr/Cloudflare)
BASE_RPC_URL = "https://base.org"

async def monitor_base_chain():
    # Inicializa cliente HTTP/2 assíncrono para reutilização de conexões (Keep-Alive)
    async with httpx.AsyncClient(http2=True) as client:
        print("🔌 Conectado ao nó público da Base L2. Escutando transações...")
        
        ultimo_bloco_processado = 0
        
        while True:
            try:
                # Payload JSON-RPC para buscar o número do bloco mais recente
                payload_bloco = {
                    "jsonrpc": "2.0",
                    "method": "eth_blockNumber",
                    "params": [],
                    "id": 1
                }
                
                response = await client.post(BASE_RPC_URL, json=payload_bloco)
                bloco_hex = response.json()['result']
                bloco_atual = int(bloco_hex, 16)
                
                # Se um novo bloco foi minerado na rede Base, extraímos os dados brutas dele
                if bloco_atual > ultimo_bloco_processado:
                    if ultimo_bloco_processado == 0:
                        ultimo_bloco_processado = bloco_atual - 1
                        
                    for num_bloco in range(ultimo_bloco_processado + 1, bloco_atual + 1):
                        payload_detalhes = {
                            "jsonrpc": "2.0",
                            "method": "eth_getBlockByNumber",
                            "params": [hex(num_bloco), True], # True traz todas as transações completas
                            "id": 2
                        }
                        
                        resp_detalhes = await client.post(BASE_RPC_URL, json=payload_detalhes)
                        bloco_dados = resp_detalhes.json().get('result')
                        
                        if bloco_dados and bloco_dados.get('transactions'):
                            transacoes = bloco_dados['transactions']
                            print(f"📦 BLOCO PROVADO | Número: {num_bloco} | Contém {len(transacoes)} transações.")
                            
                            for tx in transacoes:
                                valor_wei = int(tx.get('value', '0x0'), 16)
                                valor_eth = valor_wei / 10**18
                                
                                # Filtro Avançado: Monitora movimentações expressivas na L2 (> 5 ETH)
                                if valor_eth > 5.0:
                                    hash_tx = tx.get('hash')
                                    origem = tx.get('from')
                                    destino = tx.get('to')
                                    print(f"🚨 MOVIMENTAÇÃO WEB3 | {valor_eth:.2f} ETH transferidos! | hash: {hash_tx[:10]}...")
                                    
                    ultimo_bloco_processado = bloco_atual
                    
            except Exception as erro:
                print(f"❌ Erro na requisição RPC: {erro}")
                
            # A Base gera blocos a cada ~2 segundos. Ajustamos o pooling para evitar rate-limit.
            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(monitor_base_chain())
