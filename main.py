import websocket
import json

def ao_receber_mensagem(ws, mensagem):
    # Transforma o texto bruto recebido da Binance em JSON estruturado
    dados = json.loads(mensagem)
    
    # Extrai os dados brutos da transação que acabou de acontecer
    simbolo = dados.get('s')       # Ex: BTCUSDT
    preco = dados.get('p')         # Preço do trade
    quantidade = dados.get('q')    # Quantidade negociada
    timestamp = dados.get('E')     # Horário exato do servidor
    comprador_e_o_market_maker = dados.get('m') # Direção da agressão
    
    # Filtro de baleia: Mostra no console apenas ordens maiores que 0.5 BTC
    if float(quantidade) > 0.5:
        direcao = "VENDA" if comprador_e_o_market_maker else "COMPRA"
        print(f"🚨 BALEIA DETECTADA | {simbolo} | {direcao} de {quantidade} BTC a ${preco}")
    else:
        print(f"📊 Transação Comum: {quantidade} BTC a ${preco}")

def ao_dar_erro(ws, erro):
    print(f"❌ Erro na conexão: {erro}")

def ao_fechar(ws, status_fechamento, msg_fechamento):
    print("🔒 Conexão encerrada com o servidor da Binance.")

def ao_abrir(ws):
    print("🔌 Cabo plugado! Conectado com sucesso ao fluxo de dados brutos da Binance...")

if __name__ == "__main__":
    # Endpoint oficial de WebSocket público da Binance para o stream de trades do BTCUSDT
    url_stream = "wss://://binance.com"
    
    # Inicializa o cliente WebSocket com as funções de controle
    ws = websocket.WebSocketApp(
        url_stream,
        on_open=ao_abrir,
        on_message=ao_receber_mensagem,
        on_error=ao_dar_erro,
        on_close=ao_fechar
    )
    
    # Mantém o script rodando infinitamente escutando a rede
    ws.run_forever()
