payout=70
for i in range(9+1):
    if i>0:
        v = 2**i
        x = (100-payout)*v/100
        print(i,"-",x+v,"|",v)