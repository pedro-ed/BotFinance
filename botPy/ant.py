import GetCadle, iqLogin,time,GetPares,iqOperation,Timer,json,time,os,re
os.system('CLS')
api = iqLogin.login()
pares = GetPares.index(api,True)

for par in pares:
  velas = GetCadle.getCandle(api,1000,time.time(),1,par)
  velas_c = []
  for vela in velas:direction =1 if vela == 'verde' else 0 if vela == 'vermelha' else 2;velas_c.append(direction)
  velas = velas_c
  print(velas)
  for i in velas:
    
  break



