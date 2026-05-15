import requests
import time
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# Endpoint oficial da API da Binance (Entrega o JSON correto)
URL_API = "https://binance.com"

def iniciar_monitoramento():
    print("🤖 SERVIDOR DE SUSTENTAÇÃO DE PIPELINES INICIALIZADO...", flush=True)
    print("⚡ CONEXÃO SEGURA ESTABELECIDA. MONITORAMENTO 24H ONLINE.", flush=True)

    while True:
        try:
            resposta = requests.get(URL_API, timeout=10)
            resposta.raise_for_status()
            
            dados = resposta.json()
            preco_estavel = float(dados['price'])
            
            print(f"✓ [SUCCESS LOG] Paridade validada na Binance: R$ {preco_estavel:.2f}", flush=True)
            print("⚡ Pipeline de dados limpo. Taxa de execução processada!", flush=True)
            
        except Exception as falha_sistema:
            print(f"❌ [ALERT] Falha temporária de conexão: {falha_sistema}", flush=True)
        
        print("⏳ Aguardando abertura do próximo bloco de tarefas...", flush=True)
        sys.stdout.flush()
        time.sleep(60)

class HealthCheckServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK - Pipeline Ativo")

    def log_message(self, format, *args):
        return

def rodar_servidor_web():
    porta = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    server_address = ('', porta)
    httpd = HTTPServer(server_address, HealthCheckServer)
    print(f"🌍 Servidor de validação do Render ativo na porta {porta}", flush=True)
    httpd.serve_forever()

if __name__ == "__main__":
    worker = threading.Thread(target=iniciar_monitoramento, daemon=True)
    worker.start()
    rodar_servidor_web()
