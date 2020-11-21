def index(api):
    par = api.get_all_open_time()
    pares = []
    for paridade in par['turbo']:
        if par['turbo'][paridade]['open'] == True:
            pares.append(paridade)        
    return pares