import random
#inicio do jogo

print("----------------------------------")
print('BEM VINDO AO JOGO DA ADVINHAÇÃO!!')
print("----------------------------------")
#tentativas e numero random
tentativa = 0
numero = random.randint(0, 30)
#repetição do codigo a cada erro do usuario

while True:



    chute = int(input("Insira sua tentativa: "))

    tentativa +=1

    if chute != numero and chute > numero:

        print(f"O numero que você inseriu: {chute} não é o numero secreto! ele é menor")

    elif chute != numero and chute < numero:
        print(f"O numero que você inseriu: {chute} não é o numero secreto! ele é maior")

    elif chute == numero :
        print(f"PARABÉNS VOCÊ ACERTOU O NUMERO SECRETO com {tentativa} tentativas ")

        break







