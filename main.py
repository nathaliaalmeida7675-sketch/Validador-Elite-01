import urllib.request
import json
import time
import threading
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# --- AUTOMAÇÃO 1: Monitor de Câmbio e Cripto Livre de Bloqueios ---
def escutar_dados_globais():
    # API pública da AwesomeAPI - Feita para desenvolvedores, livre de Cloudflare agressivo
    url = "https://awesomeapi.com.br"
    print("🔌 Scanner de Ativos ativado. Monitorando câmbio e cripto em tempo real...")
    
    while True:
        try:
            req = urllib.request.Request(
                url, 
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req) as resposta:
                corpo = resposta.read().decode('utf-8')
                dados = json.loads(corpo)
                
                # Extração dos dados brutos do JSON
                dolar = dados.get('USDBRL', {}).get('bid')
                euro = dados.get('EURBRL', {}).get('bid')
                btc_brl = dados.get('BTCBRL', {}).get('bid')
                
                # Converte o preço do BTC para float e formata com separador
                if btc_brl:
                    btc_formatado = f"{float(btc_brl):,.2f}".replace(",", ".")
                else:
                    btc_formatado = "N/A"

                print(f"📊 MERCADO ATUALIZADO | Dólar: R$ {dolar} | Euro: R$ {euro} | Bitcoin: R$ {btc_formatado}")
                
        except Exception as erro:
            print(f"❌ Erro na coleta de dados: {erro}")
            
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

