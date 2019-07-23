def palavras():

    palavras = []
    qtd_palavras = int(input("Digite a Quantidade de Palavras que Deseja usar no Jogo:"))

    while len(palavras) <= qtd_palavras:
        palavra = input("Digite a Palavra secreta:")
        palavras.append(palavra)
        arquivo = open("palavras.txt", "w")
        for palavras_secretas in palavras:
            arquivo.writelines(palavras_secretas + "\n")
        arquivo.close()
    print("Palavras Salvas com Sucesso!")

