from colorama import init,Fore,Back
from iq import comprar, connect, vender, indexBots, createLog, getCandle,getparidade
#Connectar
import sys
import threading
import os
from win10toast import ToastNotifier
toast = ToastNotifier()
import os
import time 
connect()
init(autoreset=True)
from datetime import datetime
PRODUCION = False

if '-P' in sys.argv:
    PRODUCION = True

print(PRODUCION)



def notfy(title,boby):
    toast.show_toast(title,boby,duration=20,icon_path=r"C:\Users\User\Pictures\Diversity-Avatars-Avatars-Robot-01.ico")

def executeBot(invest,par,direcao,timeframe,id_bot,name):
    i=0
    prejuizo = 0
    executar=True
    invest = 2
    direcao = "CALL"
    timeframe = 1
    prejuizo = 0
    balance = 0
    ganhou = 0
    rodada = 0
    report = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    x = True
    inv = 2
    inicio = datetime.now().hour
    reconection = inicio+2
    while executar:
        confirmado = ""
        horario = datetime.now()
        if horario.second == 0:
            pares = getparidade()
            for par in pares:
                velas = getCandle(4,time.time(),1,par)
                HistVelas = []
                for vela in velas:
                    timestamp = vela["from"]
                    open = vela["open"]
                    close = vela["close"]
                    if close < open:
                        result = "vermelha"
                    if close > open:
                        result = "verde"
                    if close == open:
                        result = "cinza"
                    HistVelas.append(result)
                velaAtual = HistVelas[-1]
                HistVelas[-1] = "remove"
                HistVelas.remove("remove")
                confirmado = True if len(set(HistVelas))==1 and HistVelas[0] != "cinza" else False
                # print(HistVelas,"Vela Atual:"+velaAtual,"|",confirmado,"Par",par)
                if confirmado:
                    direcao = "CALL" if HistVelas[0] == "vermelha" else "PUT"
                    # print("confirmado fazendo operação de: ",direcao)
                    inv = invest
                    lucro = vender(invest=inv,par=par,timeframe=timeframe) if direcao == "PUT" else comprar(invest=inv,par=par,timeframe=timeframe)
                    if lucro <= 0:
                        for i in range(7):
                            payout = 80
                            v = 2**(i+1)
                            inv = v+(100-payout)*v/100
                            lucro = vender(invest=inv,par=par,timeframe=timeframe) if direcao == "PUT" else comprar(invest=inv,par=par,timeframe=timeframe)
                            if lucro < 0: balance += lucro
                            if lucro > 0:
                                print(Fore.GREEN + f"Operação vitoriosa,Par:{par}, ação:{direcao},Ciclo:{i}, Lucro:{lucro}")
                                balance +=lucro
                                break
                    else:
                        balance += lucro
                        print(Fore.GREEN + f"Operação vitoriosa, ação:{direcao}, Lucro:{lucro},Balance{balance}")
                    
                    break
                    
        else:
            time.sleep(1)
        if datetime.now().hour == reconection:
            connect()
            reconection = datetime.now().hour + 2












processos = []
bots = indexBots()
for item in bots:
    investimento = bots[item]['invest']
    parMoeda = bots[item]['par']
    direction = bots[item]['direction']
    TimeFrame = bots[item]['timeFrame']
    id_bot = item
    name = bots[item]['Name']
    tipo = bots[item]['Type']
    processos.append(threading.Thread(target=executeBot, args=(investimento,parMoeda,direction,TimeFrame,id_bot,name)))


# for processo in processos:
#     
#     processo



try:
    processos[0].start()
except:
    notfy("Erro no bot","Por favor verificar")




#websocket._exceptions.WebSocketConnectionClosedException