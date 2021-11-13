import wfdb
import matplotlib
import numpy as np
import pandas as pd
import datetime



data = wfdb.rdsamp("14046")
tabela = data[0]
dicionario = data[1]

#print(tabela.size)

tempo = []
valor = 0
sig_len = tabela.size/2

for i in range(int(sig_len)):
    valor = valor + (1/128)
    tempo.append(str(datetime.timedelta(seconds=valor)))
#print(tempo)

tabela_panda = pd.DataFrame(tabela, columns = ['ECG1(mv)','ECG2(mv)'])
tabela_panda.insert(0,"hh:mm:ss",tempo,True)



# segundos = tabela.size*(1/128)/2
# minutos = segundos/60
# horas = minutos/60
print(tabela_panda)
# print(type(tabela_panda))