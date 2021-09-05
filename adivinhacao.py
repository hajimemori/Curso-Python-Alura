print("*********************************")
print("Bem vindo ao jogo de adivinhacao!")
print("*********************************")

numero_secreto = 42
total_de_tentaivas = 3
rodada = 1


for rodada in range(1, total_de_tentaivas + 1):
    print("Tentativa: {} de {}".format(rodada, total_de_tentaivas))
    chute_str = input("Digite o seu numero entre 1 e 100: ")
    chute = int(chute_str)
    print("Voce digitou", chute)

    if(chute < 1 or chute > 100):
        print("Voce deve digitar um numero entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Voce acertou")
        break
    else:
        if(maior):
            print("Voce errou! O seu chute foi maior que o numero secreto!")
        elif(menor):
            print("Voce errou! O seu chute foi menor que o numero secreto!")


print("Fim de jogo!")


