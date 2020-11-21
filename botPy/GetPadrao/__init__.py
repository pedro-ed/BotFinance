def indentificar(relat):
    confirmado = []
    for item in relat:
      par = item[0]
      seq = item[1]
      if len(set(seq))==1 and seq[0]!="cinza":
          confirmado.append([par,"V" if seq[0]=="verde" else "C"])
    return confirmado
      
      

