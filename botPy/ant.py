import GetCadle, iqLogin,time,GetPares,iqOperation,Timer,json


x = iqOperation.GT(90,10,3)
print(x)



exit()
print(Timer.hora())

par= 'EURNZD'
print("Logando")
api = iqLogin.login()
api = iqLogin.Reconnect(api)

print("Pedando Pares")


pares = GetPares.index(api,parAtivo=True)


data =[]
print("Pegando cadles")
for par in pares:
    cadles = api.get_candles(par,1,1000,time.time())
    for m in cadles:
        data.append(m)
dt = []
x = 0
print("Calculando")
for i in range(len(data)):
    opem = data[i]['open']
    close = data[i]['close']
    direction = 0 if opem > close else 1 if opem < close else 2
    dt.append({"value":direction,"open":opem,"close":close})
    x+=1

x = dt
# x = [{'value':'1'},{'value':'1'},{'value':'1'},{'value':'1'},{'value':'0'},{'value':'0'},{'value':'0'},{'value':'0'},{'value':'0'},{'value':'1'},{'value':'1'}]
x.append("ultimo")
ultimo = len(x)-1
p=0
total=0
seq = ""
for i in range(len(x)):
  if p!=0:p-=1;continue
  if x[i]['value'] == 'ultimo':continue
  at=x[i]['value']
  seq=seq+at
  for t in range(len(x)):
    if t<i or x[t] == 'ultimo':continue
    if at == x[t]['value']:p+=1
    else:
      total+=p
      p=p-1
      CloseLt = x[i+p]['close']
      OpenAt = x[i]['open']
      print(at,OpenAt-CloseLt)
      print(OpenAt,CloseLt)
      print(p)
      break
  









