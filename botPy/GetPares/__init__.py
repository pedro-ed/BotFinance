def index(api,parAtivo=False):
    par = api.get_all_open_time()
    pares = []
    for paridade in par['turbo']:
        if parAtivo:
            pares.append(paridade)
        else:
            if par['turbo'][paridade]['open'] == True:
                pares.append(paridade)        
    return pares