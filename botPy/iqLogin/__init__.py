from pyiqoptionapi import IQOption
import pyiqoptionapi
import sys
from colorama import init,Fore,Back
import logging
api = ''
def login():
    PRODUCION = False
    if '-P' in sys.argv:
        PRODUCION = True
    init(autoreset=True)
    #LOGIN
    logging.basicConfig(format='%(asctime)s %(message)s')
    global api
    api = IQOption("pedroadv991@gmail.com", "pedroadv991@")
    api.connect()
    if PRODUCION:
        api.change_balance('REAL')#PRACTICE \ REAL
        print("Iniciando em Produção")
    else:
        api.change_balance('PRACTICE')#PRACTICE \ REAL
    if api.check_connect():
        print(Fore.RED,"Api IQ Connectada com sucesso")
        return api    
    else:
        print(Fore.RED+"Erro ao se conectar");exit()


def Reconnect(api):
    api.close_connect()
    return login()

