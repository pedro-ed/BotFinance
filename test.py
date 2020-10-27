import threading
import os


def execProcess(nome_arquivo,nomedateste):
    print(nome_arquivo,nomedateste)


arquivos = ['x.py','y.py']

processos = []
for arquivo in arquivos:
    nome = "teste"
    processos.append(threading.Thread(target=execProcess, args=(arquivo,nome)))
    # Ex: adicionar o porcesso `threading.Thread(target=inicia_programa, args=('x.py',))`

for processo in processos:
    processo.start()