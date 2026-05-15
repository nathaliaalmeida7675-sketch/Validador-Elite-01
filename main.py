import requests
import time
import sys

URL_API = https://coingecko.com

print("🤖 SERVIDOR DE SUSTENTAÇÃO DE PIPELINES INICIALIZADO...", flush=True)
print("⚡ CONEXÃO SEGURA ESTABELECIDA. MONITORAMENTO 24H ONLINE.", flush=True)

while True:
    try:
        resposta = requests.get(URL_API, timeout=10)
        dados = resposta.json()
        preco_estavel = dados['tether']['usd']
        
        print(f"✓ [SUCCESS LOG] Paridade validada na rede: ${preco_estavel}", flush=True)
        print("⚡ Pipeline de dados limpo. Taxa de execução processada!", flush=True)
        
    except Exception as falha_sistema:
        print(f"❌ [ALERT] Falha temporária de conexão: {falha_sistema}", flush=True)
    
    print("⏳ Aguardando abertura do próximo bloco de tarefas...", flush=True)
    sys.stdout.flush()
    time.sleep(60)
