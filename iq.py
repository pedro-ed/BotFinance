from pyiqoptionapi import IQOption
import pyiqoptionapi
import datetime
import time
import json
import logging
from bot2 import PRODUCION
from colorama import init,Fore,Back
#manipulador do sistema 
import sys
#manipulador de tempo
from datetime import  datetime,timedelta
from time import time
import requests
import json
api = ''
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
