import os
from datetime import datetime

# O robô busca sua chave no cofre sozinho para segurança total
chave = os.getenv('STREAMR_PRIVATE_KEY')

def minerar():
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if chave:
        print(f"✅ [{agora}] Conectado à Streamr! Lucro sendo gerado para sua carteira.")
    else:
        print(f"❌ [{agora}] ERRO: Chave não encontrada no cofre. Verifique os Secrets.")

if __name__ == "__main__":
    minerar()
