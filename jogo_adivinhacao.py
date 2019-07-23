from random import randint
def jogar_adivinhacao():
   print("*"*30)
   print("**** Jogo da Adivinhação ****")
   print("*"*30)

   rodada = 1
   nivel = int(input("Digite o Nível do Jogo:\n 1 - Fácil \n2 - Médio \n3 - Difícil\n"))
   if nivel == 1:
      tentativas = 20
      numero = randint(0,100)
      print("Digite um Numero de 0 até 100:")
   elif nivel == 2:
      tentativas = 10
      numero = randint(0,50)
      print("Digite um Numero de 0 até 50:")
   elif nivel == 3:
      tentativas = 3
      numero = randint(0,10)
      print("Digite um Numero de 0 até 10:")

   while rodada <= tentativas:
      print("Tentativa {}, de {} possiveis.".format(rodada, tentativas))
      chute = int(input("Digite um Numero:"))
      print("Voce Digitou:",chute)

      acertou = chute == numero
      maior = chute > numero
      menor = chute < numero

      if acertou:
         print("Voce acertou!se Garantiu")
         break
      elif maior:
         print("Voce errou! vc digitou um numero maior.")
      elif menor:
         print("Voce errou! vc digitou um numero menor.")

      rodada = rodada +1

   print("Game Over")
   print("O numero premiado é:",numero)
   print("Suas tentativas foram:",chute)





