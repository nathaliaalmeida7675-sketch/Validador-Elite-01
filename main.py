import time
import threading
import os
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

# --- AUTOMAÇÃO 1: Monitor Interno de Infraestrutura e Performance ---
def monitorar_container():
    print("🔌 Scanner de Infraestrutura Ativado. Monitorando performance do container...")
    
    inicio_servico = time.time()
    ciclo = 0
    
    while True:
        try:
            ciclo += 1
            tempo_ativo = int(time.time() - inicio_servico)
            
            # Captura dados nativos do processo e do sistema operacional Linux do Render
            pid = os.getpid()
            threads_ativas = threading.active_count()
            plataforma = sys.platform
            Versao_python = f"{sys.version_info.major}.{sys.version_info.minor}"
            
            print(f"📊 SYSTEM METRICS | Ciclo: #{ciclo} | PID: {pid} | Threads Ativas: {threads_ativas} | Uptime: {tempo_ativo}s | Python: {versao_python}")
                
        except Exception as erro:
            print(f"❌ Erro ao coletar métricas internas: {erro}")
            
        time.sleep(15) # Atualiza a cada 15 segundos no console

# --- AUTOMAÇÃO 2: Servidor Web que Mantém o Plano do Render Grátis ---
class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Engine de Telemetria Interna Online e Operando!")

def rodar_servidor_web():
    porta = int(os.environ.get("PORT", 10000))
    server_address = ('', porta)
    httpd = HTTPServer(server_address, WebServerHandler)
    print(f"🌐 Porta {porta} aberta. Servidor Web ativo para garantir o plano 100% gratuito!")
    httpd.serve_forever()

if __name__ == "__main__":
    # Inicia o monitor de telemetria na thread de segundo plano
    thread_dados = threading.Thread(target=monitorar_container)
    thread_dados.daemon = True
    thread_dados.start()

    # Mantém o container do Render online respondendo às checagens
    rodar_servidor_web()
