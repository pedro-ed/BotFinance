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
    data.append([par,cadles])

x = 0
print("Calculando")
for item in data:
    cd = item[1]
    for i in cd:
        opem = i['open']
        close = i['close']
    x+=1

print(i)
input("Precione enter")