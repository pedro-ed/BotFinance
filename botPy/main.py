import iqLogin, iqOperation, GetCadle, GetPadrao, Timer, GetPares, time, GetProfit
#Login na IQ
api = iqLogin.login()
count = 0
#___ Parametros ___
valorBase = 2
timeframe = 1
sequenciaAlvo = 5
CicloMax = 7
profitMin = 50
while True:
    # Aguardar Momento para opção
    Timer.SleepMoment(54)
    count+=1
    # Reconectar a cada 2H
    if count>100:count=0;api=iqLogin.Reconnect()
    # Pesquisar Pares
    pares = GetPares.index(api)
    RelatVelas = []
    # Capturar Sequencias 
    for par in pares:velas = GetCadle.getCandle(api,sequenciaAlvo,time.time(),timeframe,par);RelatVelas.append([par,velas])
    #Analizo as sequenciar procurando por Padrão alvo
    confirmados = GetPadrao.indentificar(RelatVelas)
    profit = 0
    # Verificando profits
    for i in confirmados:
        p = i[0]
        profitReq = GetProfit.index(api,p)
        if profitReq > profitMin:
            profit = profitReq
            break
    if profit > profitMin:
        par = confirmados[0][0]
        action = confirmados[0][1]
        #Executar operação
        if len(confirmados)>0:
            while True:
                result=iqOperation.action(api,action,par,timeframe,valorBase)
                #Empate
                if result!=0:
                    break
            #Perda:RECUPERAÇÃO
            if result < 0:
                iqOperation.Recuperation(api,result,CicloMax,par,action,valorBase,timeframe,profit)
            #Ganho
            if result > 0:
                pass

