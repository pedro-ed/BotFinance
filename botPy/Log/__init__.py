import os
import datetime
def AddLog(lucro,cicloRec,recuperacao):
    resultado = 'win' if lucro > 0 else 'loss'
    if recuperacao:
      resultado = "recuperacao"
    hoje = datetime.datetime.now()
    date = f"{hoje.day}/{hoje.month}/{hoje.year}"
    hora = f"{hoje.hour}:{hoje.minute}:{hoje.second}"
    data = ""
    log = f"{date},{hora},{resultado},{lucro},{cicloRec}"
    varsystemCSV = r"%updcsv%"
    # path ='Log\log.csv'
    path = 'C:\IQBOTDATABASE\log.csv'
    with open(path,'r') as file:
        data = file.read()

    with open(path,'w') as file:
        file.write(data+'\n'+log)
    os.system(varsystemCSV)