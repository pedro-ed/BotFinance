import GenerateVInv
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


def Recuperation(api,result,max,par,action,invest,timeframe,profit):
    if type(result)!='int' or result>0: print(f"Operação Vitoriosa - {result}");return False
    #iniciar Recuperação
    print(f"Operação Perdedora - {result}")
    LtRecuperation= GenerateVInv.GT(profit,max)
    for valor in LtRecuperation:
        while True:
          result = action(api,action,par,timeframe,valor)
          #Empate
          if result!=0:
              break
        #Ganho
        if result > 0:
            print(f"Operação Vitoriosa - {result}")
            break
        #Perda 
            #volta