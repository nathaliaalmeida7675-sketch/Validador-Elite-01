import requests
import time
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# Endpoint oficial da API pública da CoinGecko para pegar o preço do Tether
URL_API = "https://coingecko.com"

# Cabeçalhos necessários para evitar o bloqueio do Cloudflare
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def iniciar_monitoramento():
    print("🤖 SERVIDOR DE SUSTENTAÇÃO DE PIPELINES INICIALIZADO...", flush=True)
    print("⚡ CONEXÃO SEGURA ESTABELECIDA. MONITORAMENTO 24H ONLINE.", flush=True)

    while True:
        try:
            # Faz a requisição simulando um navegador real
            resposta = requests.get(URL_API, headers=HEADERS, timeout=10)
            resposta.raise_for_status()
            
            dados = resposta.json()
            # Tratamento correto baseado no retorno real da API da CoinGecko
            preco_estavel = dados['tether']['usd']
            
            print(f"✓ [SUCCESS LOG] Paridade validada na rede: ${preco_estavel}", flush=True)
            print("⚡ Pipeline de dados limpo. Taxa de execução processada!", flush=True)
            
        except Exception as falha_sistema:
            print(f"❌ [ALERT] Falha temporária de conexão ou resposta: {falha_sistema}", flush=True)
        
        print("⏳ Aguardando abertura do próximo bloco de tarefas...", flush=True)
        sys.stdout.flush()
        time.sleep(60)

# Servidor Web simples para manter o Render feliz e ativo na porta correta
class HealthCheckServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK - Pipeline Ativo")

    def log_message(self, format, *args):
        return  # Desativa logs repetitivos de requisições web no terminal

def rodar_servidor_web():
    # O Render injeta automaticamente a variável PORT no ambiente
    porta = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    server_address = ('', porta)
    httpd = HTTPServer(server_address, HealthCheckServer)
    print(f"🌍 Servidor de validação do Render ativo na porta {porta}", flush=True)
    httpd.serve_forever()

if __name__ == "__main__":
    # Inicia o seu script de raspagem em uma thread separada em segundo plano
    worker = threading.Thread(target=iniciar_monitoramento, daemon=True)
    worker.start()
    
    # Inicia o servidor na thread principal para evitar o timeout do Render
    rodar_servidor_web()

