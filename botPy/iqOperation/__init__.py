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

def action(api,action,par,timeframe,invest):
    if action == "C":direcao = 'call' 
    if action == "V":direcao = 'put'
    entrada = invest
    status,id = api.buy(entrada, par, direcao, timeframe)
    if status:
        resultado = api.check_win_v3(id)
        return(resultado)
    else:
        return(status)
def GT(profit,max):
    pass
    valor = [2]
    LtRecuperation = []
    vb = 2
    pt = profit
    for i in range(max):
        t=0
        for c in valor:
            t+=c
        x = ((100-pt)*valor[i]/100)+valor[i]
        LtRecuperation.append(x)
        valor.append(t+vb)
    return LtRecuperation

def Recuperation(api,result,max,par,action,invest,timeframe,profit):
    if type(result)!='int' or result>0:return False
    #iniciar Recuperação
    LtRecuperation= GT(profit,max)
    Totalciclos = len(LtRecuperation)
    count = 0
    for valor in LtRecuperation:
        count+=1
        while True:
          result = action(api,action,par,timeframe,valor)
          AddLog(result,count,True)
          #Empate
          if result!=0:
              break
        #Ganho
        if result > 0:
            print(f"Recuperação Realizada com sucesso - {result}")
            AddLog(result,0,False)
            break
        #Perda 
            #volta
        if count == Totalciclos:
            print(f"Valor não recuperado")

