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
    for m in cadles:
        data.append(m)

x = 0
print("Calculando")
for item in data:
    opem = item['open']
    close = item['close']
    x+=1

print(x)
input("Precione enter")

