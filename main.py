import urllib.request
import json
import time

def monitorar_mercado():
    # URL pública da Coingecko para pegar o preço do Bitcoin, Ethereum e Solana em tempo real
    url = "https://coingecko.com"
    
    print("🔌 Monitor de Mercado iniciado. Conectando à API...")
    
    while True:
        try:
            # Faz a requisição HTTP nativa do Python (o Render gerencia isso perfeitamente)
            requisicao = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0'} # Evita bloqueios simples de bot
            )
            
            with urllib.request.urlopen(requisicao) as resposta:
                dados = json.loads(resposta.read().decode())
                
                btc = dados['bitcoin']['usd']
                eth = dados['ethereum']['usd']
                sol = dados['solana']['usd']
                
                print(f"📊 PREÇOS ON-CHAIN | BTC: ${btc} | ETH: ${eth} | SOL: ${sol}")
                
        except Exception as erro:
            print(f"❌ Falha ao buscar dados: {erro}")
            
        # O Render precisa desse intervalo de tempo para respirar e não estourar os limites
        time.sleep(10)

if __name__ == "__main__":
    monitorar_mercado()
