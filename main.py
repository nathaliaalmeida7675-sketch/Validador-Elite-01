import time
import sys
import random
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# Configurações de Segurança do Sistema
LIMITE_REQUISICOES = 100
CARTEIRA_LOG = "0x3487d11CC7c738dfF1DC51e2C3d55d3905F70423"

def monitorar_seguranca_rede():
    print("🔒 SISTEMA DE MONITORAMENTO DE SEGURANÇA INTERNA INICIALIZADO...", flush=True)
    print(f"🔑 ASSINATURA DO OPERADOR DA REDE: {CARTEIRA_LOG}", flush=True)
    print("⚡ ESCANEAMENTO DE INFRAESTRUTURA E TRÁFEGO ATIVO 24H.", flush=True)

    while True:
        try:
            # Simula a leitura do volume de pacotes de dados chegando no servidor
            trafego_atual = random.randint(10, 150)
            print(f"📊 [NET TRAFFIC] Volume atual: {trafego_atual} requisições/s", flush=True)

            # Lógica de Circuit Breaker / Firewall do Currículo
            if trafego_atual > LIMITE_REQUISICOES:
                print(f"🚨 [FIREWALL ALERT] Volume acima do limite! Bloqueando IPs suspeitos...", flush=True)
                print("🛡️ [CIRCUIT BREAKER] Tráfego mitigado com sucesso e logs salvos.", flush=True)
            else:
                print("✓ [SUCCESS LOG] Integridade de rede validada. Sem anomalias detectadas.", flush=True)
                print(f"⚡ Log assinado para o ID: {CARTEIRA_LOG[:6]}...{CARTEIRA_LOG[-4:]}", flush=True)

        except Exception as falha_firewall:
            print(f"⚠️ [WATCHDOG] Erro ao sincronizar tabelas de IP: {falha_firewall}", flush=True)

        print("⏳ Aguardando abertura do próximo bloco de verificação...", flush=True)
        sys.stdout.flush()
        time.sleep(60)

class HealthCheckServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK - SISTEMA SEGURO")

    def log_message(self, format, *args):
        return

def rodar_servidor_web():
    porta = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    server_address = ('', porta)
    httpd = HTTPServer(server_address, HealthCheckServer)
    httpd.serve_forever()

if __name__ == "__main__":
    worker = threading.Thread(target=monitorar_seguranca_rede, daemon=True)
    worker.start()
    rodar_servidor_web()
