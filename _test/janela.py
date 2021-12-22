import requests
from tkinter import *
    
janela = Tk()

#titulo
janela.title("acesso a bd")

texto_orientacao = Label(janela, text = "INSERIR VEICULOS NO BD")
texto_orientacao.grid(column=1,row=0)

## insere ID do veiculo

tk_VEICULO_ID = Label(janela, text="VEICULO_ID")
tk_VEICULO_ID.grid(column=0,row=1,)

entrada1 = Entry(janela, bd = 5)
entrada1.grid(column=0,row=2,)

## insere NOME do veiculo

tk_VEICULO_NOME = Label(janela, text="VEICULO_NOME")
tk_VEICULO_NOME.grid(column=1,row=1,)

entrada2 = Entry(janela, bd = 5)
entrada2.grid(column=1,row=2,)

## insere ID da montadora

tk_MONTADORA_ID= Label(janela, text="MONTADORA_ID")
tk_MONTADORA_ID.grid(column=2,row=1,)

entrada3 = Entry(janela, bd = 5)
entrada3.grid(column=2,row=2,)

#botao = Button(janela,text = "Adicionar ao BD", command = acao)
#botao.grid(column=3,row=2,padx=10, pady=10)

#mostra comando enviado a bd

texto_saida = Label(janela, text="")
texto_saida.grid(column=0,row=3, padx=10, pady=10)

janela.mainloop() #permite que a janela fique em loop na tela