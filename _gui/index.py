janela = Tk()

#titulo
janela.title("acesso a bd")

texto_orientacao = Label(janela, text = "clique no botao para iniciar")
texto_orientacao.grid(column=0,row=0, padx=10, pady=10)

botao = Button(janela,text = "clique", command = acao)
botao.grid(column=0,row=1,padx=10, pady=10)

entrada = Entry(janela, bd = 5)
entrada.grid(column=2,row=1,)

texto_saida = Label(janela, text="")
texto_saida.grid(column=0,row=2, padx=10, pady=10)

janela.mainloop() #permite que a janela fique em loop na tela
