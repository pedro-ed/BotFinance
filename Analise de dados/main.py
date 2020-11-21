import MetaTrader5 as mt5
mt5.initialize()

simbolos = mt5.symbols_get()


for s in simbolos:
    if 'USD' in s.name:
        print(s.name)



mt5.shutdown()