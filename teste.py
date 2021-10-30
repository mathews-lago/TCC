import matplotlib.pyplot as plt
import random
import numpy as np
import ctypes
from tkinter import *
from tkinter import messagebox
#ctypes.windll.user32.MessageBoxW(0, "Insira seu nome", "CAixa de texto", 1)
def mostrarMSg(tiposmg,msg):
    messagebox.showinfo(title="Me ajuda",message=msg)

app = Tk()
app.title("Aplicativo Health Care")
app.geometry("350x350")
app.mainloop()
#x = [24,25,26]
#y = [23,24,25]
#plt.plot(x,y)
#plt.show()
x = random.randint(10,25)
k = random.randint(60,90)
z = np.random.randint(60,60+x,(288,1))
print(z)