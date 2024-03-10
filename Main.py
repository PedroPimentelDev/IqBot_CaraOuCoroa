from iqoptionapi.stable_api import IQ_Option
from Funçoes import executarOperacao

#Configurações
saldo = 0
moeda = 'EURUSD-OTC' # Par de moeda
valor_inicial = 10 # Valor de entrada
exp = 1 # Tempo do candle
tipo = 'BINARY' #Tipo de operação
gales = int

#Conexão com a Iq options
Iq = IQ_Option("","") # Email e senha
conectar = Iq.connect()

#Feedback da tentativa de conexão
if conectar:
    print('Conectado')
else:
    print('Não foi possivel conectar')

# Loop principal de negociação
while True:

    # Executa a operação e atualiza o saldo
    valor = valor_inicial
    gales = 0
    msg, lucro = executarOperacao(moeda,valor,exp,tipo)
    saldo += lucro
    print(msg + " " +str(lucro))
    print("Saldo total: " + str(saldo))

    # Dobra o valor em caso de prejuízo
    while(lucro < 0):
        gales += 1
        valor *= 2
        msg, lucro  = executarOperacao(moeda,valor,exp,tipo)
        saldo += lucro
        print(msg + " " +str(lucro))
        print("Saldo total: " + str(saldo))
        print("Número de gales: " + str(gales))
        
        