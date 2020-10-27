from colorama import init,Fore,Back
from iq import comprar, connect, vender, indexBots, createLog
#Connectar
import threading
import os
from win10toast import ToastNotifier
toast = ToastNotifier()


connect()
init(autoreset=True)

def notfy(title,boby):
    toast.show_toast(title,boby,duration=20,icon_path=r"C:\Users\User\Pictures\Diversity-Avatars-Avatars-Robot-01.ico")



def executeBot(invest,par,direcao,timeframe,id_bot,name):
    i=0
    prejuizo = 0
    executar=True
    while executar:


        
        i+=1
        inv = invest+prejuizo
        if direcao == "PUT":
            lucro = vender(invest=inv,par=par,timeframe=timeframe)
        if direcao == "CALL":
            lucro = comprar(invest=inv,par=par,timeframe=timeframe)
        lucro = int(lucro)
        result = "Neutro"
        if lucro > 0:
            prejuizo = 0
            result = "Ganhou"
        if lucro < 0:
            result = "Perdeu"
            prejuizo += abs(lucro)+invest
        if i>40 and prejuizo <=2:
            i=0
            connect()
        createLog(ID_BOT=id_bot,result=result,direction=direcao,prejuizo=prejuizo,lucro=lucro,timeframe=timeframe,Nexec=i,investiment=invest,nameBot=name)
        
processos = []
bots = indexBots()
for item in bots:
    investimento = bots[item]['invest']
    parMoeda = bots[item]['par']
    direction = bots[item]['direction']
    TimeFrame = bots[item]['timeFrame']
    id_bot = item
    parMoeda = "EURUSD-OTC"
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