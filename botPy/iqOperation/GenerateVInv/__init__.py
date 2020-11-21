def GT(profit,max):
    pass
    valor = [2]
    LtRecuperation = []
    vb = 2
    pt = profit
    for i in range(max):
        t=0
        for c in valor:
            t+=c
        x = ((100-pt)*valor[i]/100)+valor[i]
        LtRecuperation.append(x)
        valor.append(t+vb)
    return LtRecuperation