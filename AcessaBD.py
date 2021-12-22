#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
import requests
import pandas as pd
from tkinter import *
import os
import webbrowser


# In[2]:


def add_montadora():
    
    query_INPUT_MONTADORA_ID = INPUT_MONTADORA_ID.get()
    query_INPUT_MONTADORA_NOME = INPUT_MONTADORA_NOME.get()
    
    check1 = verifica_id(query_INPUT_MONTADORA_ID,'MONTADORA_ID', 'montadoras')

    check2 = verifica_nome(query_INPUT_MONTADORA_NOME,'MONTADORA_NOME','montadoras')

    if (check1 == 1 and check2 == 1):
        query = "insert into montadoras values(" + query_INPUT_MONTADORA_ID +""",'"""+query_INPUT_MONTADORA_NOME+"');"

        cursor.execute(query)
        con_.commit()
        
        end = Tk()
        
        mensagem = Label(end,text = "Montadora incluida com sucesso!!!")
        mensagem.grid(column=0,row=0,padx=10, pady=10)
        
        end.mainloop() 
        
    else:
        warning = Tk()
        
        mensagem_aviso = Label(warning,text = "Não foi possivel inserir montadora pois ID ou Nome ja existem!")
        mensagem_aviso.grid(column=0,row=0,padx=10, pady=10)
        
        warning.mainloop() 


# In[3]:


def rmv_todos_veiculos_montadora():
    
    query_INPUT_MONTADORA_ID = INPUT_MONTADORA_ID.get()
    
    query = """DELETE FROM montadoras WHERE MONTADORA_ID ="""+query_INPUT_MONTADORA_ID+ ";"

    cursor.execute(query)
    con_.commit()
    
    df = pd.read_sql( """select * from """+ 'veiculos' +""";""", con = con_)
    df = df.loc[df['MONTADORA_ID'] == int(query_INPUT_MONTADORA_ID)]
    lista_ids_rmv = df["VEICULO_ID"]
    lista_ids_rmv = list(lista_ids_rmv)
    
    for i in range(len(lista_ids_rmv)):
        query = """DELETE FROM veiculos WHERE VEICULO_ID = """+ str(lista_ids_rmv[i])+ ";"

        cursor.execute(query)
        con_.commit() 
        

    end = Tk()

    mensagem = Label(end,text = "Montadora e veiculos excluidos com sucesso!!!")
    mensagem.grid(column=0,row=0,padx=10, pady=10)

    end.mainloop()


# In[4]:


def confirma_rmv_veiculos():
    
    warning_rmv = Toplevel()

    mensagem_aviso = Label(warning_rmv,text = "ATENCAO!!! Ao excluir esta montadora, todos os veiculos contidos nela serão removidos também, deseja mesmo continuar?") 
    mensagem_aviso.grid(column=0,row=0,padx=10, pady=10)

    bnt_rmv_todos_veiculos = Button(warning_rmv,text = "REMOVER VEICULOS", command = rmv_todos_veiculos_montadora)
    bnt_rmv_todos_veiculos.grid(column=0,row=1,padx=10, pady=10)
    
    bnt_cancela = Button(warning_rmv,text = "CANCELAR", command = warning_rmv.destroy)
    bnt_cancela.grid(column=0,row=2,padx=10, pady=10)

    warning_rmv.mainloop() 
    


# In[5]:


def rmv_montadora():
    
    query_INPUT_MONTADORA_ID = INPUT_MONTADORA_ID.get()
    
    check1 = verifica_id(query_INPUT_MONTADORA_ID,'MONTADORA_ID', 'montadoras')
    
    if (check1 == 0):
        
        confirma_rmv_veiculos()
        
    else:
        warning = Tk()
        
        mensagem_aviso = Label(warning,text = "Não foi possivel excluir montadora pois esta montadora não existe!")
        mensagem_aviso.grid(column=0,row=0,padx=10, pady=10)
        
        warning.mainloop() 
        


# In[6]:


def add_veiculo():
    
    query_INPUT_VEICULO_ID = INPUT_VEICULO_ID.get()
    query_INPUT_VEICULO_NOME = INPUT_VEICULO_NOME.get()
    query_INPUT_VEICULO_MONTADORA_ID = INPUT_VEICULO_MONTADORA_ID.get()
    
    check1 = verifica_id(query_INPUT_VEICULO_ID,'VEICULO_ID', 'veiculos')

    check2 = verifica_nome(query_INPUT_VEICULO_NOME,'VEICULO_NOME','veiculos')
    
    check3 = verifica_id(query_INPUT_VEICULO_MONTADORA_ID,'MONTADORA_ID', 'montadoras')
    
    if (check1 == 1 and check2 == 1):
        if (check3 == 0):
            
            query = "insert into veiculos values(" + query_INPUT_VEICULO_ID +""",'"""+query_INPUT_VEICULO_NOME+"""',"""+query_INPUT_VEICULO_MONTADORA_ID+");"
    
            cursor.execute(query)
            con_.commit()
            
            end = Tk()
        
            mensagem = Label(end,text = "veiculo incluido com sucesso!!!")
            mensagem.grid(column=0,row=0,padx=10, pady=10)
        
            end.mainloop()    
        else:
            warning = Tk()
        
            mensagem_aviso = Label(warning,text = "Não foi possivel incluir veiculo pois este ID de montadora não existe!")
            mensagem_aviso.grid(column=0,row=0,padx=10, pady=10)
        
            warning.mainloop() 
    else:
        warning = Tk()
        
        mensagem_aviso = Label(warning,text = "Não foi possivel incluir veiculo pois ID ou Nome ja existem!")
        mensagem_aviso.grid(column=0,row=0,padx=10, pady=10)
        
        warning.mainloop() 
        


# In[7]:


def rmv_veiculo():
    
    query_INPUT_VEICULO_ID = INPUT_VEICULO_ID.get()
    
    check1 = verifica_id(query_INPUT_VEICULO_ID,'VEICULO_ID', 'veiculos')
    
    if (check1 == 0):
        query = """DELETE FROM veiculos WHERE VEICULO_ID ="""+query_INPUT_VEICULO_ID+ ";"

        cursor.execute(query)
        con_.commit()
        
        end = Tk()
        
        mensagem = Label(end,text = "Veiculo excluido com sucesso!!!")
        mensagem.grid(column=0,row=0,padx=10, pady=10)
        
        end.mainloop() 
    else:
        warning = Tk()
        
        mensagem_aviso = Label(warning,text = "Não foi possivel excluir veiculo pois este veiculo não existe!")
        mensagem_aviso.grid(column=0,row=0,padx=10, pady=10)
        
        warning.mainloop() 
        


# In[8]:


def gera_relatorio():
    df = pd.read_sql( """select * from veiculos inner join montadoras on veiculos.MONTADORA_ID = montadoras.MONTADORA_ID;""", con = con_)
    df = df.drop(columns=['MONTADORA_ID'])
    df.to_html('RELATORIO.html')
    #pdf.from_url('RELATORIO.html', 'Relatorio.pdf')
    webbrowser.open('RELATORIO.html', new= 2)


# In[9]:


def verifica_id(ID,coluna,tabela):
     
    df = pd.read_sql( """select * from """+ tabela +""";""", con = con_)
    lista_id = df[coluna]
    for i in range (len(lista_id)):
        if lista_id[i] == int(ID):
            return 0
    return 1


# In[10]:


def verifica_nome(NOME,coluna,tabela):
    df = pd.read_sql( """select * from """+ tabela +""";""", con = con_)
    lista_nome = df[coluna]
    for i in range (len(lista_nome)):
        if lista_nome[i] == str(NOME):
            return 0
    return 1


# In[22]:





# In[11]:


def conector():
    INPUT_USER = USER_ID.get()
    INPUT_PASSWORD = PASSWORD_ID.get()

    USER_IDf = str(INPUT_USER)
    PASSWORD_IDf = str(INPUT_PASSWORD)
    global con_
    global cursor
    con_ = mysql.connector.connect(host='localhost',database='car_table',user= USER_IDf,password= PASSWORD_IDf)
    
    if con_.is_connected():
        cursor = con_.cursor()
        grid_30["text"] = "conectado"
        print('conectado')
    else:
        print('desconectado')
        grid_30["text"] = "desconectado"
    login.destroy()


# In[13]:


login = Tk()

login.title("login")

#grid_00 = Label(login, text = "Insira as informações de login e senha para acessar o banco de dados")
#grid_00.grid(column=0,row=0, padx=10, pady=10)

grid_10 = Label(login, text = "user")
grid_10.grid(column=0,row=1, padx=10, pady=10)

grid_11 = Label(login, text = "password")
grid_11.grid(column=1,row=1, padx=10, pady=10)

USER_ID = Entry(login, bd = 5)
USER_ID.grid(column=0,row=2, padx=10, pady=10)

PASSWORD_ID = Entry(login, bd = 5)
PASSWORD_ID.grid(column=1,row=2, padx=10, pady=10)

BTN_CANCEL = Button(login,text = "Cancelar", command = login.destroy)
BTN_CANCEL.grid(column=0,row=3,padx=10, pady=10)

BTN_LOGIN = Button(login,text = "Entrar", command = conector)
BTN_LOGIN.grid(column=1,row=3,padx=10, pady=10)

janela = Tk()

#titulo
janela.title("acesso a bd")


grid_00 = Label(janela, text = "")
grid_00.grid(column=0,row=0, padx=10, pady=10)

grid_10 = Label(janela, text = "TECNOMOTOR")
grid_10.grid(column=1,row=0, padx=10, pady=10)

grid_20 = Label(janela, text = "status BD:")
grid_20.grid(column=2,row=0, padx=10, pady=10)

grid_30 = Label(janela, text = "",bg="green")
grid_30.grid(column=3,row=0, padx=10, pady=10)


#montadora
ADD_MONTADORA_LABEL = Label(janela,text = "Montadora")
ADD_MONTADORA_LABEL.grid(column=0,row=1,padx=10, pady=10)


MONTADORA_ID = Label(janela,text = "MONTADORA_ID")
MONTADORA_ID.grid(column=0,row=2, padx=10, pady=10)

MONTADORA_NOME = Label(janela,text = "MONTADORA_NOME")
MONTADORA_NOME.grid(column=1,row=2, padx=10, pady=10)


INPUT_MONTADORA_ID = Entry(janela, bd = 5)
INPUT_MONTADORA_ID.grid(column=0,row=3,padx=10, pady=10)

INPUT_MONTADORA_NOME = Entry(janela, bd = 5)
INPUT_MONTADORA_NOME.grid(column=1,row=3,padx=10, pady=10)

BTN_ADD_MONTADORA = Button(janela,text = "Add Montadora", command = add_montadora)
BTN_ADD_MONTADORA.grid(column=2,row=3,padx=10, pady=10)

BTN_RMV_MONTADORA = Button(janela,text = "Rmv Montadora", command = rmv_montadora)
BTN_RMV_MONTADORA.grid(column=3,row=3,padx=10, pady=10)

#Veiculo
VEICULO_LABEL = Label(janela,text = "Veiculo")
VEICULO_LABEL.grid(column=0,row=4,padx=10, pady=10)


VEICULO_ID = Label(janela,text = "VEICULO_ID")
VEICULO_ID.grid(column=0,row=5, padx=10, pady=10)

VEICULO_NOME = Label(janela,text = "VEICULO_NOME")
VEICULO_NOME.grid(column=1,row=5, padx=10, pady=10)

VEICULO_MONTADORA_ID = Label(janela,text = "MONTADORA_ID")
VEICULO_MONTADORA_ID.grid(column=2,row=5, padx=10, pady=10)



INPUT_VEICULO_ID = Entry(janela, bd = 5)
INPUT_VEICULO_ID.grid(column=0,row=6,padx=10, pady=10)

INPUT_VEICULO_NOME = Entry(janela, bd = 5)
INPUT_VEICULO_NOME.grid(column=1,row=6,padx=10, pady=10)

INPUT_VEICULO_MONTADORA_ID = Entry(janela, bd = 5)
INPUT_VEICULO_MONTADORA_ID.grid(column=2,row=6,padx=10, pady=10)

BTN_ADD_VEICULO = Button(janela,text = "Add Veiculos", command = add_veiculo)
BTN_ADD_VEICULO.grid(column=3,row=6,padx=10, pady=10)

BTN_RMV_VEICULO = Button(janela,text = "Rmv Veiculos", command = rmv_veiculo)
BTN_RMV_VEICULO.grid(column=4,row=6,padx=10, pady=10)

texto_saida = Label(janela, text="")
texto_saida.grid(column=0,row=7, padx=10, pady=10)

BTN_RELATORIO = Button(janela,text = "Gerar Relatorio", command = gera_relatorio)
BTN_RELATORIO.grid(column=0,row=8,padx=10, pady=10)

janela.mainloop() #permite que a janela fique em loop na tela


# In[ ]:





# In[ ]:




