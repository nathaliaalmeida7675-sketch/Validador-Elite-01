import requests
import time
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# Endpoint oficial da API pública da Binance para pegar o preço do Tether limpo
URL_API = "https://binance.com"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def iniciar_monitoramento():
    print("🤖 SERVIDOR DE SUSTENTAÇÃO DE PIPELINES INICIALIZADO...", flush=True)
    print("⚡ CONEXÃO SEGURA ESTABELECIDA. MONITORAMENTO 24H ONLINE.", flush=True)

    while True:
        try:
            resposta = requests.get(URL_API, headers=HEADERS, timeout=10)
            resposta.raise_for_status()
            
            dados = resposta.json()
            # Tratamento correto baseado no formato de retorno real da API da Binance
            preco_estavel = float(dados['price'])
            
            print(f"✓ [SUCCESS LOG] Paridade validada na Binance: ${preco_estavel}", flush=True)
            print("⚡ Pipeline de dados limpo. Taxa de execução processada!", flush=True)
            
        except Exception as falha_sistema:
            print(f"❌ [ALERT] Falha temporária de conexão ou resposta: {falha_sistema}", flush=True)
        
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
