from iqoptionapi.stable_api import IQ_Option
import random

def conectarIq(email, senha):
    iq = IQ_Option(email, senha)
    conectado = iq.connect()
    if conectado[0]:
        print('Conectado')
    else:
        print('Não foi possível conectar')
    return iq, conectado[0]

#Escolhe a direção de entrada
def estrategia():
    caracoroa = random.randint(1, 2)
    if caracoroa == 1:
        dir = 'CALL'
        print("\nCOMPRA")
    else:
        dir = 'PUT'
        print("\nVENDA")
    return dir

#Realiza a compra
def comprar(iq, moeda, dir, valor, exp, tipo):
    if tipo == "DIGITAL":
        id = iq.buy_digital_spot_v2(moeda, valor, dir, exp)
    else:
        id = iq.buy(valor, moeda, dir, exp)
    return id[1]

#Verifica o resultado da operacao em andamento
def verificar_resultado(iq, tipo, id):
    while True:
        if tipo == "DIGITAL":
            resultado = iq.check_win_digital_v2(id)
        elif tipo == "BINARY":
            resultado = iq.check_win_v4(id)
        else:
            return "Tipo de operação inválido", 0

        if resultado[1] is not None:
            lucro = round(resultado[1], 2)
            if lucro > 0:
                msg = "Vitória =)"
            else:
                msg = "Derrota =( Vamos pra próxima"
            return msg, lucro

#Resume em uma unica funcao 
def executarOperacao(iq, moeda, valor, exp, tipo):
    dir = estrategia()
    id = comprar(iq, moeda, dir, valor, exp, tipo)
    return verificar_resultado(iq, tipo, id)
