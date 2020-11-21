def AddLog(log):
    data = ""
    path ='Log\log.csv'
    with open(path,'r') as file:
        data = file.read()

    with open(path,'w') as file:
        file.write(data+'\n'+log)
    print(data)



AddLog("teste55")