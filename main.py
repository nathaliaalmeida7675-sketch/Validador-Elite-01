import urllib.request
import json
import time
import threading
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# --- AUTOMAÇÃO 1: Monitor de Cripto Sem Bloqueio de IP ---
def escutar_dados_globais():
    # Rota pública alternativa da CoinGecko
    url = "https://coingecko.com"
    print("🔌 Scanner de Ativos ativado. Monitorando preços globais...")
    
    while True:
        try:
            # Usando uma string simples de User-Agent padrão
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            )
            with urllib.request.urlopen(req) as resposta:
                dados = json.loads(resposta.read().decode())
                btc = dados.get('bitcoin', {}).get('usd')
                eth = dados.get('ethereum', {}).get('usd')
                print(f"📊 DADOS EM TEMPO REAL | BTC: ${btc} | ETH: ${eth}")
                
        except Exception as erro:
            print(f"❌ Erro na coleta: {erro}")
            
        time.sleep(30) # Intervalo seguro de 30 segundos

# --- AUTOMAÇÃO 2: Servidor Web que Mantém o Plano do Render Grátis ---
class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Engine de Dados Online e Operando com Sucesso!")

def rodar_servidor_web():
    porta = int(os.environ.get("PORT", 10000))
    server_address = ('', porta)
    httpd = HTTPServer(server_address, WebServerHandler)
    print(f"🌐 Porta {porta} aberta. Servidor Web ativo para garantir o plano 100% gratuito!")
    httpd.serve_forever()

if __name__ == "__main__":
    thread_dados = threading.Thread(target=escutar_dados_globais)
    thread_dados.daemon = True
    thread_dados.start()

    rodar_servidor_web()
