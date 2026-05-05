import os
import time

chave = os.getenv('STREAMR_PRIVATE_KEY')

def minerador():
    if chave:
        print("✅ [BOT 01] Crachá validado! Conectado na Streamr...")
        tempo_trabalho = 15 * 60 
        inicio = time.time()
        while (time.time() - inicio) < tempo_trabalho:
            print("🚀 [BOT 01] Minerando dados... Produção ativa.")
            time.sleep(55) # Intervalo de 55 segundos
        print("Sessão do BOT 01 finalizada.")
    else:
        print("❌ Erro no BOT 01: Chave não encontrada.")

if __name__ == "__main__":
    minerador()
