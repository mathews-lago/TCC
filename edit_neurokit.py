from math import inf
import neurokit2 as nk
import pandas as pd
import matplotlib.pyplot as plt


# plt.rcParams['figure.figsize'] = [15, 9]  # Bigger images
# plt.rcParams['font.size']= 13
# Recebe os dados
# data = pd.read_csv("https://raw.githubusercontent.com/neuropsychology/NeuroKit/master/data/bio_resting_5min_100hz.csv")
jeff = pd.read_csv('Jeff.csv')
carlos = pd.read_csv('Carlos.csv')
# Cria variável do tipo <class 'pandas.core.frame.DataFrame'> ecg_signals
# Cria variável do tipo <class 'dict'> info

def processa_plota(dados):
    # Process ecg
    ecg_signals, info = nk.ecg_process(dados["ECG"], sampling_rate=128)
    plot = nk.ecg_plot(ecg_signals[:2000], sampling_rate=100)

    # Process rsp
    # rsp_signals, info = nk.rsp_process(data["RSP"], sampling_rate=100)
    # plot = nk.rsp_plot(rsp_signals[:2000], sampling_rate=100)
    print("789")
    saida = ecg_signals
    return saida


def quebrar_dados(ecg_signals):
    # Cria dicionário contendo as duas metades do dado completo. 
    # Cada metade é uma variável do tipo <class 'pandas.core.frame.DataFrame'> epochs['1'] e epochs['2']
    epochs = nk.epochs_create(ecg_signals, events=[0, 3000], sampling_rate=128, epochs_start=150, epochs_end=200)

    # Cria uma variável contendo uma das metades de epoch_signals do tipo <class 'pandas.core.frame.DataFrame'>
    metade1 = epochs['1']

    metade1.to_csv('metade2_carlos_epochs.csv') #Cria arquivo csv com a metade da tabela

    print('chegou!!')
    return metade1


metade1 = quebrar_dados(carlos)
processa_plota(metade1)
plt.show()

# print("Dados metade")
print(metade1)
# print("tamanho arquivo completo")
# print(jeff.size)
# print("tamanho arquivo metade")
# print(metade1.size)
# print("tipo arquivo metade")
# print(type(metade1))
