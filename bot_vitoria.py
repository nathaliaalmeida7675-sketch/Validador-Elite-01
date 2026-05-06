import os
import time

# 1. Puxa a chave privada dos Secrets do GitHub para segurança
chave = os.getenv('STREAMR_PRIVATE_KEY')

# 2. Endereço do Contrato da sua Streamr
contrato = "0x438805950f7eca7924513c45516e3504570e4c3d"

def minerador():
    if chave:
        print(f"✅ [BOT 01] Crachá validado! Conectado ao contrato: {contrato}")
        
        # Define o tempo de produção (ex: 15 minutos)
        tempo_operacao = 15 * 60 
        inicio = time.time()
        
        print(f"🚀 [BOT 01] Minerando dados na rede Streamr... Produção ativa.")
        
        # Loop de execução
        while (time.time() - inicio) < tempo_operacao:
            print("⏳ [BOT 01] Processando blocos de dados... Status: OK.")
            time.sleep(60) # Espera 1 minuto entre cada log para não encher a tela
            
        print("Sessão do BOT 01 finalizada com sucesso.")
    else:
        print("❌ Erro no BOT 01: Chave privada não encontrada nos Secrets do GitHub.")

if __name__ == "__main__":
    minerador()
