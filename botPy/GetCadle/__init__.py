def getCandle(api,nC,time,timeframe,par):
    """
    Captura Candles
    """
    HistVelas =[]
    for vela in api.get_candles(par,(timeframe * 60),nC,time):
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
    return HistVelas
