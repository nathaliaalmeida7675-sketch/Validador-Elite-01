import urllib.request
import json
import time
import threading
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

# --- AUTOMACÃO 1: Scanner de Terremotos Globais em Tempo Real ---
def escutar_dados_globais():
    # API do Serviço Geológico dos EUA (USGS) - Dados brutos atualizados a cada minuto
    url = "https://usgs.gov"
    print("🔌 Scanner Global Ativado. Monitorando abalos na crosta terrestre...")
    
    hashes_processados = set() # Evita duplicar alertas no log
    
    while True:
        try:
            requisicao = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(requisicao) as resposta:
                dados = json.loads(resposta.read().decode())
                
                eventos = dados.get('features', [])
                
                for evento in eventos:
                    properties = evento.get('properties', {})
                    id_evento = evento.get('id')
                    
                    if id_evento not in hashes_processados:
                        magnitude = properties.get('mag')
                        local = properties.get('place')
                        gols = properties.get('tsunami')
                        
                        # Filtro Técnico Avançado: Alerta apenas para abalos relevantes (> 2.0)
                        if magnitude and float(magnitude) >= 2.0:
                            alerta_tsunami = "⚠️ RISCO DE TSUNAMI!" if gols == 1 else "Seguro"
                            print(f"🚨 IMPACTO DETECTADO | Magnitude: {magnitude} | Local: {local} | Status: {alerta_tsunami}")
                        
                        hashes_processados.add(id_evento)
                        
        except Exception as erro:
            print(f"❌ Falha ao coletar dados globais: {erro}")
            
        # Limpa o cache para não estourar a memória do container gratuito do Render
        if len(hashes_processados) > 500:
            hashes_processados.clear()
            
        time.sleep(30) # Coleta controlada a cada 30 segundos

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
    # Inicia a captura de dados brutos na Thread de segundo plano
    thread_dados = threading.Thread(target=escutar_dados_globais)
    thread_dados.daemon = True
    thread_dados.start()

    # Segura o container do Render online de graça na porta certa
    rodar_servidor_web()
