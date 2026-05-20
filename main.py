import urllib.request
import json
import time
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# --- TAREFA 1: O Monitor de Preço (Roda em segundo plano) ---
def monitorar_mercado():
    url = "https://coingecko.com"
    print("🔌 Monitor de Mercado iniciado na nuvem...")
    
    while True:
        try:
            requisicao = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(requisicao) as resposta:
                dados = json.loads(resposta.read().decode())
                btc = dados['bitcoin']['usd']
                eth = dados['ethereum']['usd']
                sol = dados['solana']['usd']
                print(f"📊 PREÇOS ON-CHAIN | BTC: ${btc} | ETH: ${eth} | SOL: ${sol}")
        except Exception as erro:
            print(f"❌ Falha ao buscar dados: {erro}")
        
        time.sleep(15) # Intervalo seguro de 15 segundos

# --- TAREFA 2: O Servidor Web Fake (Atende às exigências do Render Grátis) ---
class ServidorFake(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Automacao Online e Respondendo!")

def rodar_servidor_web():
    # O Render injeta automaticamente a porta necessária na variável 'PORT'
    import os
    porta = int(os.environ.get("PORT", 10000))
    server_address = ('', porta)
    httpd = HTTPServer(server_address, ServidorFake)
    print(f"🌐 Servidor Web ativo respondendo na porta {porta} para manter o plano gratis...")
    httpd.serve_forever()

if __name__ == "__main__":
    # 1. Inicia o monitor de preços em uma Thread separada (segundo plano)
    thread_monitor = threading.Thread(target=monitorar_mercado)
    thread_monitor.daemon = True
    thread_monitor.start()

    # 2. Roda o servidor web na thread principal para o Render ficar feliz
    rodar_servidor_web()
