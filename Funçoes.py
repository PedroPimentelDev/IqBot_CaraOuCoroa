from iqoptionapi.stable_api import IQ_Option
Iq = IQ_Option("","") # Email e senha
conectar = Iq.connect()
import random

#Defini o cara ou coroa
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
def comprar(moeda, dir, valor, exp, tipo):
    if tipo == "DIGITAL":
        id = Iq.buy_digital_spot_v2(moeda, valor, dir, exp)
    else:
        id = Iq.buy(valor, moeda, dir, exp)
    return id[1]

#Verifica o resultado da operacao em andamento
def verificarResultado(tipo, id):
    while True:
        if tipo == "DIGITAL":
            resultado = Iq.check_win_digital_v2(id)
        elif tipo == "BINARY":
            resultado = Iq.check_win_v4(id)
        else:
            break

        if resultado[1] is not None and resultado[1] > 0:
            msg = ("Estouramo a boca e os pcr fez a boa", resultado[1])
            break
        elif resultado[1] is not None and resultado[1] < 0:
            msg = ("Deu trave vm pra próxima", resultado[1])
            break
        elif resultado[1] is not None and resultado[1] == 0:
            msg = ("Deu trave vm pra próxima", resultado[1])
            break
    return msg

#Resume em uma unica funcao 
def executarOperacao(moeda, valor, exp, tipo):
    dir = estrategia()
    id = comprar(moeda, dir, valor, exp, tipo)
    msg = verificarResultado(tipo, id)
    return(msg)
