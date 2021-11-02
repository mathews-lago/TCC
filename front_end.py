try:
    from tkinter import *
except:
    from tkinter import *

janela1 = Tk()

def pac_cadastro():
    global nome
    global idade
    global sexo
    global peso
    global altura
    nome = Entrada1.get()
    idade = Entrada2.get()
    sexo = Entrada3.get()
    peso = Entrada4.get()
    altura = Entrada5.get()

    if  nome in ' ':
        Entrada1['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        Entrada1['bg'] = 'white'
    if  idade in ' ':
        Entrada2['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        Entrada2['bg'] = 'white'
    if  sexo in ' ':
        Entrada3['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        Entrada3['bg'] = 'white'
    if  peso in ' ':
        Entrada4['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        Entrada4['bg'] = 'white'
    if  altura in ' ':
        Entrada5['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        Entrada5['bg'] = 'white'
    if  nome != '' and  idade != '' and  sexo != '' and peso != '' and altura != '' :
        janela1.destroy()

titulo1 = Label(bg='#191970', font=('Arial', '12', 'bold'), fg='white', text='Bem vindo ao Health Care, favor inserir os seguintes dados.')
titulo1.place(x='13', y='10')

Entrada1 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
Entrada1.place(x=100, y=50)
Info1 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Nome:')
Info1.place(x=10, y=50)

Entrada2 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
Entrada2.place(x=100, y=75)
Info2 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Idade:')
Info2.place(x=10, y=75)

Entrada3 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
Entrada3.place(x=100, y=100)
Info3 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Sexo:')
Info3.place(x=10, y=100)

Entrada4 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
Entrada4.place(x=100, y=125)
Info4 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Peso(Kg):')
Info4.place(x=10, y=125)

Entrada5 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
Entrada5.place(x=100, y=150)
Info5 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Altura(m):')
Info5.place(x=10, y=150)

erro = Label(bg='#191970', fg='red', font=('Arial', '11'), text='')
erro.place(x=135, y=175)

salvar = Button(width='39', text='Salvar', font=('Arial','10'), command=pac_cadastro)
salvar.place(x=15, y=200)

janela1.resizable(width=False, height=False)
janela1.configure(bg='#191970')
janela1.title('Aplicativo Health Care')
janela1.geometry('472x290+450+450')
janela1.mainloop()

janela2 = Tk()

def resp_cadastro():
    global nome_ac
    global tel_ac
    global email_ac

    nome_ac = Entrada1.get()
    tel_ac = Entrada2.get()
    email_ac = Entrada3.get()

    if  nome_ac in ' ':
        Entrada1['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        Entrada1['bg'] = 'white'
    if  tel_ac in ' ':
        Entrada2['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        Entrada2['bg'] = 'white'
    if  email_ac in ' ':
        Entrada3['bg'] = 'pink'
        erro['text'] = 'Preencha todos os campos!'
    else:
        Entrada3['bg'] = 'white' 
    if  nome_ac != '' and  tel_ac != '' and  email_ac != '':
        janela2.destroy()

titulo1 = Label(bg='#191970', font=('Arial', '12', 'bold'), fg='white', text='Favor inserir os dados do responsável:')
titulo1.place(x='13', y='10')

Entrada1 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
Entrada1.place(x=100, y=50)
Info1 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Nome:')
Info1.place(x=10, y=50)

Entrada2 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
Entrada2.place(x=100, y=75)
Info2 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Telefone:')
Info2.place(x=10, y=75)

Entrada3 = Entry(width=25, bg='white', font=('Comic Sans MS', '10'))
Entrada3.place(x=100, y=100)
Info3 = Label(font=('Arial', '11', 'bold'), fg='white', bg='#191970', text='Email:')
Info3.place(x=10, y=100)

erro = Label(bg='#191970', fg='red', font=('Arial', '11'), text='')
erro.place(x=135, y=125)

salvar = Button(width='39', text='Salvar', font=('Arial','10'), command=resp_cadastro)
salvar.place(x=15, y=150)

janela2.resizable(width=False, height=False)
janela2.configure(bg='#191970')
janela2.title('Aplicativo Health Care')
janela2.geometry('450x290+350+350')
janela2.mainloop()