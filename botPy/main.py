import iqLogin, iqOperation, GetCadle, GetPadrao, Timer, GetPares, time, GetProfit,Log
#Login na IQ
api = iqLogin.login()
countRec = 0
#___ Parametros ___
valorBase = 4
timeframe = 1
sequenciaAlvo = 8
CicloMax = 10
profitMin = 75
MomentAction = 52
reconnectN = 100
while True:
    # Aguardar Momento para opção
    # Log.LogAlert("Aguardar Momento para opção",'INFO')
    Timer.SleepMoment(MomentAction)
    countRec+=1
    # Reconectar a cada 2H
    if countRec>reconnectN:countRec=0;api=iqLogin.Reconnect(api)
    # Pesquisar Pares
    # Log.LogInfo("   Pesquisar Pares",'INFO')
    pares = GetPares.index(api)
    RelatVelas = []
    # Capturar Sequencias 
    # Log.LogInfo("   Capturar Sequencias",'INFO')
    for par in pares:velas = GetCadle.getCandle(api,sequenciaAlvo,time.time(),timeframe,par);RelatVelas.append([par,velas])
    #Analizo as sequenciar procurando por Padrão alvo
    # Log.LogInfo("   procurando por Padrão alvo",'INFO')
    confirmados = GetPadrao.indentificar(RelatVelas)
    profit = 0
    # Verificando profits
    # Log.LogInfo("   Verificando profits",'INFO')
    for i in confirmados:
        p = i[0]
        profitReq = GetProfit.index(api,p)
        if profitReq > profitMin:
            profit = profitReq
            break
    if profit > profitMin:
        par =   confirmados[0][0]
        action = confirmados[0][1]
        #Gerar Lista
        # Log.LogInfo("   Gerar Lista",'INFO')
        LtValue = iqOperation.GT(profit,CicloMax,valorBase)
        #Executar operação
        # Log.LogInfo("   Executar operação",'INFO')
        if len(confirmados)>0:
            values = [0]
            #Ciclo de Execuções
            for i in range(CicloMax):
                #Definição de valor de investimento
                value = sum(values)+valorBase
                x = ((100-profit)*value/100)+value
                values.append(value)
                #Empate value == 0
                doji = True
                while doji:
                    result=iqOperation.action(api,action,par,timeframe,value)
                    doji = True if result == 0 else False
                # GANHOU
                    Log.AddLog(result,LtValue.index(value)+1,False,action,value)
                    if result > 0:
                        Log.LogAlert(f"Operação Vitoriosa: {value}",'INFO','verde')
                        break
                Log.LogAlert(f"Recuperando: {value}",'INFO','amarelo')


