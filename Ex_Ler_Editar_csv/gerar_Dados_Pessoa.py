import csv
import random
import pandas as pd

def cadastro(novo_cadastro):
    with open('clientes.csv','a',newline='') as csv_file:
        
        campos = ['id','nome','sobrenome','tipo','data de nascimento',
            'cpf','rua','numero','complemento','cep','telefone 1','telefone 2','e-mail']
        escreveCsv = csv.DictWriter(csv_file,fieldnames=campos,delimiter=',')

        #escreveCsv.writeheader()
        escreveCsv.writerow(novo_cadastro)


#Utilizando loop iterando por todas as linhas do arquivo antes de printar
def ler_cadastro1(file_Name):
    with open(file_Name,'r') as ler_csv_file:
        lerCsv = csv.DictReader(ler_csv_file)

        coluna = []

        for linhas in lerCsv:
            coluna.append(linhas['frequencia'])
        print(coluna)

#ler uma celula específica do arquivo. Necessita das coordenadas linha e coluna
def ler_cadastro2(tempo,file_Name):
    ler = pd.read_csv(file_Name)
    pesquisa = ler.loc[tempo,'frequencia']
    print('frequencia no tempo %s '  % tempo + '= %s' % pesquisa)



def inserir_Dados(file_Name):
    # with open(file_Name,'r') as ler_csv_file:
    #     lerCsv = csv.DictReader(ler_csv_file)

        with open(file_Name, 'a', newline='') as editar_csv_file:

            campos = ['tempo','frequencia','nome','idade','peso','altura']
            editar_csv_file = csv.DictWriter(editar_csv_file,fieldnames=campos,delimiter=',')

            #editar_csv_file.writeheader()
            
            #Simula os dados que seriam recebidos diáriamente.
            #Depois preciso de método para receber uma lista e adicioná-la ao arquivo como incremento.

            freq =[]
            tempo =[]
            for i in range(10):

                x = random.randint(10,25)
                k = random.randint(60,90)
                z = random.randint(60,60+x)

                freq.append(z)
            
                tempo.append(i)
            for i in range(len(freq)):
                editar_csv_file.writerow({'tempo':tempo[i],'frequencia':freq[i]})

def compara(tempo,frequencia):
    ler = pd.read_csv("tbl_freq_padrao.csv")
    pesquisa = ler.loc[tempo,'frequencia']
    diferença = abs(int(frequencia) - int(pesquisa))
    
    if ( diferença > 10):
        print("Diferença para padrão maior que 10bpm")
        return[True,diferença]
    else:
        print("Diferença para padrão menor que 10bpm")
        return[False,diferença]

cad_theus = {'id':'1','nome':'Matheus','sobrenome':'Cerqueira','tipo':'Paciente',
    'data de nascimento':'23081994',
    'cpf':'44455566677','rua':'dos Bobos','numero':'11','complemento':'','cep':'13060999',
    'telefone 1':'19988888888','telefone 2':'','e-mail':'matheus12cerqueira@hotmail.com'}

cad_maths = {'id':'2','nome':'Mathews','sobrenome':'Lago','tipo':'Responsavel',
    'data de nascimento':'02021997',
    'cpf':'11122233388','rua':'dos Bobos','numero':'80085','complemento':'Apt 31','cep':'69696969',
    'telefone 1':'11911223344','telefone 2':'','e-mail':'jocabesta@bestabesta'}

# cadastro(cad_maths)
# inserir_Dados('joao.csv')
ler_cadastro1('carlos.csv')
ler_cadastro2(9,'carlos.csv')

