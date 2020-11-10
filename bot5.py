from pyiqoptionapi import IQOption
import pyiqoptionapi
import datetime
import time
import json
import logging

from colorama import init,Fore,Back
#manipulador do sistema 
import sys
#manipulador de tempo
from datetime import  datetime,timedelta
from time import time
import requests
import json
api = ''
from colorama import init,Fore,Back
# from iq import comprar, connect, vender, indexBots, createLog, getCandle,getparidade
#Connectar
import sys
import threading
import os
from win10toast import ToastNotifier
toast = ToastNotifier()
import os
import time 

PRODUCION = False

if '-P' in sys.argv:
    PRODUCION = True


def connect():
    init(autoreset=True)
    #LOGIN
    logging.basicConfig(format='%(asctime)s %(message)s')
    global api
    api = IQOption("pedroadv991@gmail.com", "pedropedroka")
    api.connect()
    if PRODUCION:
        api.change_balance('REAL')#PRACTICE \ REAL
    else:
        api.change_balance('PRACTICE')#PRACTICE \ REAL
    if api.check_connect():
        return True
    else:
        return False

def comprar(invest,par,timeframe):
    entrada = invest
    direcao = 'call'
    status,id = api.buy(entrada, par, direcao, timeframe)
    if status:
        resultado = api.check_win_v3(id)
        return(resultado)
    else:
        return(status)


def vender(invest,par,timeframe):
    entrada = invest
    direcao = 'put'
    status,id = api.buy(entrada, par, direcao, timeframe)
    if status:
        resultado = api.check_win_v3(id)
        return(resultado)
    else:
        return(status)



def indexBots():
    url = "https://apibots-937d3.firebaseio.com/Botmanager/Bots.json"
    payload = ""
    response = requests.request("GET", url, data=payload)
    return json.loads(response.text)    

def createLog(ID_BOT,result,direction,prejuizo,lucro,timeframe,Nexec,investiment,nameBot):
    url = "https://apibots-937d3.firebaseio.com/Botmanager/Logs.json"
    headers = {'content-type': 'application/json'}
    payload = {
                "createdAt":time(),
                "ID_Bot":ID_BOT,
                "nameBot":nameBot,
                "balanceTotal":api.get_balance(),
                "result":result,
                "direction":direction,
                "prejuizo":prejuizo,
                "lucro":lucro,
                "timeFrame":timeframe,
                "NumExecution":Nexec,
                "investiment":investiment
                }
    response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
    return (response.text)


def getCandle(nC,time,timeframe,par):
    """
    Captura Candles
    """
    return api.get_candles(par,(timeframe * 60),nC,time)




def getparidade():
    par = api.get_all_open_time()
    pares = []
    for paridade in par['turbo']:
        if par['turbo'][paridade]['open'] == True:
            pares.append(paridade)
    return pares


def reconnectIQ():
    api.close_connect()
    # connect()



def notfy(title,boby):
    toast.show_toast(title,boby,duration=20,icon_path=r"C:\Users\User\Pictures\Diversity-Avatars-Avatars-Robot-01.ico")

connect()
init(autoreset=True)
from datetime import datetime








def executeBot(invest,par,direcao,timeframe,id_bot,name):
    i=0
    prejuizo = 0
    executar=True
    invest = 2
    direcao = "CALL"
    timeframe = 1
    balance = 0
    ganhou = 0
    rodada = 0
    report = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    x = True
    inv = 2
    inicio = datetime.now().hour
    reconection = inicio+2
    initBalance = api.get_balance()
    while executar:
        confirmado = ""
        horario = datetime.now()
        if horario.second == 55:
            pares = getparidade()
            for par in pares:
                velas = getCandle(6,time.time(),1,par)
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
                if confirmado:
                    direcao = "CALL" if HistVelas[0] == "vermelha" else "PUT"
                    if direcao == "CALL":
                        inv= 3 
                        print(Fore.GREEN+f"{direcao} - PADRÃO ENCONTRADO {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}|{par}")
                        lucro = vender(invest=inv,par=par,timeframe=timeframe) if direcao == "PUT" else comprar(invest=inv,par=par,timeframe=timeframe)
                    else:
                        print(Fore.RED+f"{direcao} - PADRÃO ENCONTRADO {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}|{par}")
                        lucro = vender(invest=inv,par=par,timeframe=timeframe) if direcao == "PUT" else comprar(invest=inv,par=par,timeframe=timeframe)
                    if lucro > 0:
                        print("")
                    if lucro < 0:
                        for ciclo in range(8):
                            inv = 3**ciclo+1
                            lucro = vender(invest=inv,par=par,timeframe=timeframe) if direcao == "PUT" else comprar(invest=inv,par=par,timeframe=timeframe)
                            if lucro > 0:
                                break
                    break           
        else:
            time.sleep(1)
        os.system('cls')
        balanceAtual = api.get_balance()
        print(balanceAtual-initBalance)
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


#12.470

#websocket._exceptions.WebSocketConnectionClosedException