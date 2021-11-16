from math import inf
import neurokit2 as nk
import pandas as pd
import matplotlib.pyplot as plt
import wfdb
import numpy as np
import datetime
import os
from os.path import exists
from os import mkdir


plt.rcParams['figure.figsize'] = [15, 9]  # Bigger images
plt.rcParams['font.size']= 13

#Definte diretório a ser lido
diretorio = "mit-bih-arrhythmia-database-1.0.0"

# Gera arquivo csv a partir de um waveform
def wfdb_csv(paciente):
    data = wfdb.rdsamp(paciente) #tupla
    tabela = data[0] #tabela ndarray
    dicionario = data[1]
    tempo = []
    valor = 0
    sig_len = tabela.size/2

    for i in range(int(sig_len)):
        valor = valor + (1/360)
        tempo.append(str(datetime.timedelta(seconds=valor)))

    tabela_panda = pd.DataFrame(tabela, columns = ['ECG','ECG2(mv)'])
    tabela_panda.insert(0,"hh:mm:ss",tempo,True)
    tabela_panda.to_csv(paciente + '.csv',index=False)

#processa o ECG no formato .csv, plota imagem e salva como figura
def processa_plota(dados,tempoT,fs):
    # Process ecg
    ecg_signals, info = nk.ecg_process(dados["ECG"], sampling_rate=fs)
    plot = nk.ecg_plot(ecg_signals[:tempoT*fs], sampling_rate=fs)

    # Process rsp
    # rsp_signals, info = nk.rsp_process(data["RSP"], sampling_rate=100)
    # plot = nk.rsp_plot(rsp_signals[:2000], sampling_rate=100)
    print("789")
    saida = ecg_signals
    return saida

#Seleciona uma janela de tempo dentro do arquivo csv para análise
def quebrar_dados(dataframe_arquivo,tempoT,fs,t_plot_ini,t_plot_fin):
    # Cria dicionário contendo as duas metades do dado completo. 
    # Cada metade é uma variável do tipo <class 'pandas.core.frame.DataFrame'> epochs['1'] e epochs['2']
    epochs = nk.epochs_create(dataframe_arquivo, events=[0, tempoT*fs], sampling_rate=fs,
                                 epochs_start=t_plot_ini, epochs_end=t_plot_fin)

    # Cria uma variável contendo uma das metades de epoch_signals do tipo <class 'pandas.core.frame.DataFrame'>
    metade1 = epochs['1']

    metade1.to_csv('Jorge_epochs_min2.csv') #Cria arquivo csv com a metade da tabela

    print('chegou!!')
    return metade1

#Altera Variáveis para gerar 30 janelas de 1 minuto
def janela_1minx30(nome,dataframe):
    tempoT = 130
    fs = 128
    t_plot_ini = 0
    t_plot_fin = 60
    
    for i in range(30):
        t_plot_ini = 60*i
        t_plot_fin = 60 + 60*i
        
        metade1 = quebrar_dados(dataframe,tempoT,fs,t_plot_ini,t_plot_fin)
        ecg_process = processa_plota(metade1,tempoT,fs)

        dir_out = dir + nome + "_plots/"
        if not exists(dir_out):
            mkdir(dir_out)
        plt.savefig(dir_out + nome + str(i+1) + '.png')
        ecg_process.to_csv('ECG_Processado/' + nome[:-4] + '_ECG_Process' + str(i+1) + '.csv')
        # plt.show()

#Rotina para listar os arquivos wfdb
def listar_arquivos(dir):
    lista_nomes = [file for file in os.listdir(dir) if ".dat" in file]
    return lista_nomes

#Start
arquivos = listar_arquivos(diretorio)
for i in range(len(arquivos)):
    nome = arquivos[i][:-4]
    wfdb_csv(nome) #Cria arquivo .csv
    dataframe_arquivo = pd.read_csv(nome + ".csv") #Cria um dataframe para o arquivo selecionado no loop
    janela_1minx30(nome,dataframe_arquivo) #Inicia o loop de 30 janelas que chamara as outras funções




    
# janela_1minx30(file,arritimia)

