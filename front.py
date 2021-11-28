from math import inf
import neurokit2 as nk
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
import wfdb_neurokit as processa
import numpy as np

plt.rcParams['figure.figsize'] = [15, 9]  # Bigger images
plt.rcParams['font.size']= 13

dados = pd.DataFrame(pd.read_csv("422.csv")) #16265 caso grave
hrv = pd.DataFrame(pd.read_csv("rate_422.csv"))

rate_max = 0
rate_min = 200
x = 0
fs = 250

def divide_tempo(dados,hrv,fs):
    epochs1 = nk.epochs_create( dados, events=[0, 60*fs],
                                sampling_rate=fs,
                                epochs_start=600,
                                epochs_end=660)

    dados_1min = epochs1['1'].to_csv('422_min1.csv') #Cria arquivo csv com a metade da tabela
    dados_1min = pd.DataFrame(pd.read_csv('422_min1.csv')) #Cria Dataframe a partir do csv

    epochs2 = nk.epochs_create( hrv, events=[0, 60*fs],
                                sampling_rate=fs,
                                epochs_start=0,
                                epochs_end=60)
    
    hrv_1min = epochs2['1'].to_csv('rate_422_min1.csv') #Cria arquivo csv com a metade da tabela
    hrv_1min = pd.DataFrame(pd.read_csv("rate_422_min1.csv")) #Cria Dataframe a partir do csv
    
    return dados_1min,hrv_1min

def min_max(hrv_1min,sig_len,rate_max,rate_min,x):
    for i in range(int(sig_len)):
        x = hrv_1min['ECG_Rate'][i]
        if x < rate_min:
            rate_min = x
        if x > rate_max:
            rate_max = x
    return rate_min,rate_max

def processa_plota(dados_1min,fs):
    # Process ecg
    print('chegou2')
    ecg_signals, info = nk.ecg_process(dados_1min["ECG(mv)"], sampling_rate=fs)
    plot = nk.ecg_plot(ecg_signals,sampling_rate=fs)
    plt.show()
    print('chegou3')
    return ecg_signals

dados_1min,hrv_1min = divide_tempo(dados,hrv,fs)
sig_len = hrv_1min.size/5
print("chegou " + str(sig_len))
rate_min,rate_max = min_max(hrv_1min,sig_len,rate_max,rate_min,x)
rate_mean = hrv_1min["ECG_Rate"].mean()
bla = processa_plota(dados_1min,fs)
peaks = np.where(bla["ECG_R_Peaks"] == 1)[0]

print("Rate max: " + str(rate_max))
print("Rate min: " + str(rate_min))
print("Rate mean: " + str(rate_mean))
print("Peaks: " + str(peaks.size))

aviso=Tk()

#def popup_alerta():
if rate_mean > 100:
    mensagem = 'Frequência cardíaca alta!!\nSintoma: Taquicardia'
    cor = '#ff0000'
    fonte_alerta = "Helvetica 12 bold"
    fonte_info = "Helvetica 12 bold"
    cor_aviso = "#fff8dc"
elif rate_mean < 50:
    mensagem = 'Frequência cardíaca baixa!!\nSintoma Braquicardia'
    cor = '#ff0000'
    fonte_alerta = "Helvetica 12 bold"
    fonte_info = "Helvetica 12 bold"
    cor_aviso = "#fff8dc"
elif rate_max > 100 and rate_min < 50:
    mensagem = 'Grande variação de frequencia cardiaca'
    cor = '#cdad00'
    fonte_alerta = "Helvetica 12 bold"
    fonte_info = "Helvetica 12 bold"
    cor_aviso = "#fff8dc"
else:
    mensagem = 'Frequência cardíaca normal'
    cor = '#2e8b57' #verde
    fonte_alerta = "Helvetica 12 bold"
    fonte_info = "Helvetica 12 bold"
    cor_aviso = "#ffffff"

largura_aviso = 350
altura_aviso = 200
aviso.title("Status do Paciente")
aviso.geometry(str(largura_aviso) + "x" + str(altura_aviso))
aviso.configure(background="#fff8dc")

tarja=Label(aviso,text='', background=cor, foreground="#fff8dc")
tarja.place(relx=0.5,rely=0.2,anchor="center",width=(largura_aviso),height=60)
alerta=Label(aviso,text = mensagem, font= fonte_alerta, background=cor,foreground=cor_aviso)
alerta.place(relx=0.5,rely=0.2,anchor="center",width=largura_aviso,height=60)

infos=Label(aviso,text = "Batimentos por minuto: \t" + str(int(peaks.size)) + 
                        "\nMaior Frequência: \t\t" + str(int(rate_max)) + 
                        "\nMenor Frequencia: \t" + str(int(rate_min)) +
                        "\nFrequencia Média: \t" + str(int(rate_mean)),
                        font = fonte_info,
                        background='#fff8dc',
                        foreground="#000",
                        justify="left")
infos.place(relx=0.5,rely=0.6,anchor="center",width=largura_aviso,height=100)

aviso.mainloop()
print('chegou')
#popup_alerta()
processa_plota(dados_1min,fs)
print('chegou 4')
plt.show()
