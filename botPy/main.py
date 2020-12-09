import iqLogin, iqOperation, GetCadle, GetPadrao, Timer, GetPares, time, GetProfit,Log,GetConfg
#Login na IQ
api = iqLogin.login()
countRec = 0
while True:
    #___ Parametros ___
    CONFIG = GetConfg.index()
    valorBase = CONFIG['valorBase'];timeframe = CONFIG['timeframe'];sequenciaAlvo = CONFIG['sequenciaAlvo'];CicloMax = CONFIG['CicloMax'];profitMin = CONFIG['profitMin'];MomentAction = CONFIG['MomentAction'];reconnectN = CONFIG['reconnectN']
    # Aguardar Momento para opção
    Timer.SleepMoment(MomentAction)
    countRec+=1
    # Reconectar a cada 2H
    if countRec>reconnectN:countRec=0;api=iqLogin.Reconnect(api)
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
        par    = confirmados[0][0]
        action = confirmados[0][1]
        #Gerar Lista
        LtValue = iqOperation.GT(profit,CicloMax,valorBase)
        #Executar operação
        if len(confirmados)>0:
            values = []
            #Ciclo de Execuções
            for i in range(CicloMax):
                #Definição de valor de investimento
                value = sum(values)+valorBase
                value = ((100-profit)*value/100)+value
                values.append(value)
                #Empate value == 0
                doji = True
                while doji:
                    result=iqOperation.action(api,action,par,timeframe,value)
                    doji = True if result == 0 else False
                    # GANHOU
                    Log.AddLog(result,i+1,False,action,value)
                if result > 0:Log.LogAlert(f"Operação Vitoriosa: {value}",'INFO','verde');break
                Log.LogAlert(f"Recuperando: {value}",'INFO','amarelo')


