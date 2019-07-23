import jogo_adivinhacao
import jogo_forca
import palavras

print("*"*35)
print("******* Locadora do Cobra ********")
print("*"*35)

print("Escolha seu Jogo")
print("(1) Jogo da Adivinhação  (2) Jogo da Forca")

jogo = int(input("Defina o Jogo que vc quer Jogar:"))

if(jogo == 1):
   print("jogando adivinhação")
   jogo_adivinhacao.jogar_adivinhacao()
elif(jogo == 2):
   print("(1) para jogar jogo da forca\n (2) para cadastrar palavras")
   option = int(input("Escolha uma Opção:"))
   if(option == 1):
      jogo_forca.jogar_forca()
   elif(option == 2):
      print("Salvar Palavras")
      palavras.palavras()