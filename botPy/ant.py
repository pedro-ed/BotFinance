import GetCadle, iqLogin,time,GetPares,iqOperation,Timer,json
from datetime import datetime
from dateutil import tz






exit()
def timestamp_data(x,separador): # Função para converter timestamp
	hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%Y'+separador+'%m'+separador+'%d'), '%Y'+separador+'%m'+separador+'%d')
	# hora = hora.replace(tzinfo=tz.gettz('GMT'))	
	return str(hora)[:-6]


def timestamp_hora(x,separador): # Função para converter timestamp
	hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime('%H'+separador+'%M'+separador+'%s'), '%H'+separador+'%M'+separador+'%s')
	hora = hora.replace(tzinfo=tz.gettz('GMT'))	
	return str(hora)[:-6]


print(timestamp_data(1605726842,"/"))

exit()
# timestamp = 1605726842000
# timestamp = 1545730073
# dt_object = datetime.fromtimestamp(timestamp)
# print("dt_object =", dt_object)
# print("type(dt_object) =", type(dt_object))
# exit()

print("Logando")
api = iqLogin.login()
 

status,historico = api.get_position_history_v2('digital-option',3,0,0,0)
import json
from datetime import datetime
dateHoje = datetime.now().strftime("%m/%d/%Y")
lucroHoje = 0
for item in historico['positions']:
  FINAL_OPERACAO= item['close_time']
  INICIO_OPERACAO= item['open_time']
  LUCRO = item['close_profit']
  ENTRADA = item['invest']
  PARIDADE= item['raw_event']['instrument_underlying']
  DIRECAO = item['raw_event']['instrument_dir']
  VALOR = item['raw_event']['buy_amount']
  date = datetime.fromtimestamp(int(str(INICIO_OPERACAO)[:10])).strftime("%m/%d/%Y")
  hora = datetime.fromtimestamp(int(str(INICIO_OPERACAO)[:10])).strftime("%H:%M:%S")
  print(dateHoje,date)
  if dateHoje == date:
    print("foi")
    lucroHoje+=LUCRO
    pass
  break
 
print(lucroHoje)





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
  









