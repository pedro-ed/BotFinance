from colorama import init,Fore,Back
from iq import comprar, connect, vender, indexBots, createLog
#Connectar
import threading
import os
from win10toast import ToastNotifier
toast = ToastNotifier()
import os

connect()
init(autoreset=True)

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
    balance = 100
    ganhou = 0
    perdaseguida = 0
    report = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    x = True
    while executar:
        #---Invesão programada --- #
        for item in range(15):
            if perdaseguida == item:
                report[item] +=1 
    
        if perdaseguida == 3:i = 1 if i == 0 else 0
    
        i = 1 if i == 0 else 0
        if i == 1:direcao  = "PUT"
        if i == 0 : direcao = "CALL"
        #-----------#

        i+=1
        inv = 2**perdaseguida
        inv += 1 if inv == 1 else inv

        if direcao == "PUT":
            lucro = vender(invest=inv,par=par,timeframe=timeframe)
        if direcao == "CALL":
            lucro = comprar(invest=inv,par=par,timeframe=timeframe)
        lucro = int(lucro)

        result = "Neutro"

        if lucro > 0:
            prejuizo = 0
            perdaseguida = 0
            result = "Ganhou"

        if lucro < 0:
            result = "Perdeu"
            perdaseguida +=1
            prejuizo += abs(lucro)
        
        if i>40 and prejuizo <=2:
            i=0
            connect()
        createLog(ID_BOT=id_bot,result=result,direction=direcao,prejuizo=prejuizo,lucro=lucro,timeframe=timeframe,Nexec=i,investiment=invest,nameBot=name)
        t = 0
        porcent = 0
        total = 0
        os.system("cls")
        for i in report:
            quant = i
            valor = 2**t+10
            total +=quant
            print(Fore.BLUE+ f"{t}x Paguei R${valor}, {quant} vezes")
            t += 1 
        print(total)
        print(report)
        













processos = []
bots = indexBots()
for item in bots:
    investimento = bots[item]['invest']
    parMoeda = bots[item]['par']
    parMoeda = "EURUSD-OTC"
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