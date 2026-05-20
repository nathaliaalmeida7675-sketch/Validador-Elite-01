import time
import threading
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# --- AUTOMACÃO 1: Engine de Processamento Numérico Computacional ---
def processamento_interno():
    print("🔌 Engine Computacional Ativado. Calculando ciclos de performance...")
    
    ciclo = 0
    inicio = time.time()
    
    while True:
        try:
            ciclo += 1
            uptime_segundos = int(time.time() - inicio)
            
            # Executa um calculo matematico simples para gerar telemetria interna
            fator_computacional = (ciclo * 104729) % 999983
            
            print(f"📊 METRICS | Ciclo: #{ciclo} | Fator: {fator_computacional} | Uptime: {uptime_segundos}s | Status: ESTÁVEL")
                
        except Exception:
            pass
            
        time.sleep(15) # Executa estritamente a cada 15 segundos

# --- AUTOMAÇÃO 2: Servidor Web Nativo para o Render Grátis ---
class ServidorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Engine Computencial Online!")

def rodar_servidor_web():
    # Coleta a porta injetada pelo ambiente do Render
    porta_render = int(os.environ.get("PORT", 10000))
    endereco = ('', porta_render)
    httpd = HTTPServer(endereco, ServidorHandler)
    print(f"🌐 Servidor Web escutando na porta {porta_render} de forma nativa.")
    httpd.serve_forever()

if __name__ == "__main__":
    # 1. Start na Thread de processamento puro
    thread_computacional = threading.Thread(target=processamento_interno)
    thread_computacional.daemon = True
    thread_computacional.start()

    # 2. Start no servidor para manter o status LIVE estável
    rodar_servidor_web()
