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
from tkinter import messagebox

plt.rcParams['figure.figsize'] = [15, 9]  # Bigger images
plt.rcParams['font.size']= 13

dados = pd.DataFrame(pd.read_csv("108.csv"))
hrv = pd.DataFrame(pd.read_csv("rate_108.csv"))
rate_max = 0
rate_min = 200
x = 0
fs = 360

def min_max(hrv_1min,sig_len,rate_max,rate_min,x):
 for i in range(int(sig_len)):
     x = hrv_1min['ECG_Rate'][i]
     if x < rate_min:
      rate_min = x
     if x > rate_max:
      rate_max = x
 return rate_min,rate_max

def divide_tempo(dados,hrv,fs):
 epochs1 = nk.epochs_create(dados, events=[0, 60*fs], sampling_rate=fs,epochs_start=0, epochs_end=60)
 dados_1min = epochs1['1'].to_csv('108_min1.csv')
 dados_1min = pd.DataFrame(pd.read_csv('108_min1.csv')) #Cria arquivo csv com a metade da tabela

 epochs2 = nk.epochs_create(hrv, events=[0, 60*fs], sampling_rate=fs,epochs_start=0, epochs_end=60)
 hrv_1min = epochs2['1'].to_csv('rate_108_min1.csv')
 hrv_1min = pd.DataFrame(pd.read_csv("rate_108_min1.csv")) #Cria arquivo csv com a metade da tabela
 
 return dados_1min,hrv_1min

def processa_plota(dados_1min,fs):
 # Process ecg
 ecg_signals, info = nk.ecg_process(dados_1min["ECG(mv)"], sampling_rate=fs)
 plot = nk.ecg_plot(ecg_signals,sampling_rate=fs)

dados_1min,hrv_1min = divide_tempo(dados,hrv,fs)
print(dados_1min)
print(hrv_1min)
sig_len = hrv_1min.size/4
print(sig_len)
rate_min,rate_max = min_max(hrv_1min,sig_len,rate_max,rate_min,x)
processa_plota(dados_1min,fs)
plt.show()
print(rate_min)
print(rate_max)

if rate_max > 100 and rate_min < 50:
 messagebox.showinfo('Aviso\n','Grande variação de frequencia cardiaca')