import random

def jogar():

    print("Bem vindo ao jogo de adivinha !")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("qual o nivel de dificulcudade ?")
    print("(1) facil (2) medio (3) dificil")

    nivel = int(input("Defina o nivel :"))

    if(nivel==1):
        total_de_tentativas = 20
    elif(nivel==2):
        total_de_tentativas = 10
    else:
        total_de_tentativas =5
        
    for rodada in range (1, total_de_tentativas + 1):    
        print ("Tentativa {} de {} " .format(rodada, total_de_tentativas ))
        chute_str = input("Digite o seu numero : ")
        print("voce digitou" , chute_str)
        chute = int(chute_str)
        
        if (chute < 1 or chute > 100) :
            print("Voce deve digitar um nimero entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        
        if (acertou):
            print ("voce acertou e fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print ("voce errou ! o seu chute foi maior do que o numneor secrteto ")
            
            elif (menor):
                print ("voce errou ! o seu chute foi menor do que o numneor secrteto ")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
                
        print ("Fim de jogo!")

if(__name__=="__main__"):
    jogar()       
        