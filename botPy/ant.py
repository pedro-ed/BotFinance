import GetCadle, iqLogin,time,GetPares
par= 'EURNZD'
print("Logando")
api = iqLogin.login()
print("Pedando Pares")
pares = GetPares.index(api,parAtivo=True)


data =[]
print("Pegando cadles")
for par in pares:
    cadles = api.get_candles(par,1,1000,time.time())
    data.append([x for x in cadles])

x = 0
print("Calculando")
for item in data:
    opem = item['open']
    close = item['close']
    x+=1

print(x)
input("Precione enter")