import adivinhacao
import forca

def escolher_jogo():
    print("*************************************")
    print("********Escolha seu jogo************ ")
    print("*************************************")

    print("(1) forca (2) Adivinhacao") 

    jogo = int(input("Qual o jogo?"))

    if(jogo == 1):
        print("jogando foca")
        forca.jogar()
    elif(jogo == 2):
        print("jogando adivinha")
        adivinhacao.jogar()
        
if (__name__ == "__main__" ) :
    escolher_jogo()       