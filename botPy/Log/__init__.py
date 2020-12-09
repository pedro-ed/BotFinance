import os
import datetime
import requests
import json
def hora():
    agora = datetime.datetime.now()
    return agora.strftime("%H:%M:%S")

def AddLog(lucro,cicloRec,recuperacao,direcao,value):
    resultado = 'win' if lucro > 0 else 'loss'
    if recuperacao:
      resultado = "recuperacao"
    hoje = datetime.datetime.now()
    date = f"{hoje.day}/{hoje.month}/{hoje.year}"
    hora = f"{hoje.hour}:{hoje.minute}:{hoje.second}"
    data = ""
    log = f"{date},{hora},{resultado},{lucro},{cicloRec},{direcao}"
    url = "https://apibots-937d3.firebaseio.com/Botmanager/Logs.json"

    payload = {
		"id":round(int(hoje.day+hoje.second+hoje.hour+hoje.minute)),
		"data":f"{date}",
		"hora":f"{hora}",
		"resultado":resultado,
		"lucro":lucro,
		"direcao":direcao,
        "investiment":value
    }
    payload = json.dumps(payload)
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 200:
        return True
    else:
      return response.status_code


from colorama import init,Fore,Back 
init(autoreset=True)


def LogAlert(msg,type,cor):
  if cor == 'amarelo':print(Fore.LIGHTYELLOW_EX+f"[{type} - {hora()} ] => {msg}")
  if cor == 'verde':print(Fore.LIGHTGREEN_EX+f"[{type} - {hora()} ] => {msg}")


def LogInfo(msg,type):
  print(Fore.LIGHTBLUE_EX+f"[{type} - {hora()} ] => {msg}")
