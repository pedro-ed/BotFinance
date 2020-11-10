payout=70
f = [0]
x = 5
for i in range(9):
    v =0
    f.append(v)
    if i>0:
        i = x
        for i in range(len(f)-1):
            v +=f[i]
        
        
        print(f,v)