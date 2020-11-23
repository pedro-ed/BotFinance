import GetCadle, iqLogin,time,GetPares,iqOperation,Timer

print(Timer.hora())

par= 'EURNZD'
print("Logando")
api = iqLogin.login()

print("Reconnectando")

api = iqLogin.Reconnect(api)
if api.check_connect():
  print("Reconectado com sucesso")
exit()
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
for i in range(len(data)):
    opem = data[i]['open']
    close = data[i]['close']
    direction = 0 if opem > close else 1 if opem < close else 2

print(x)
input("Precione enter")

