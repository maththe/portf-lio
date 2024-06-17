import random
pont1 = 0
pont2 = 0
resultado1 = ('JOGADOR1 VENCEU!')
resultado2 = ('JOGADOR2 VENCEU!')
print('Boas-vindas!')
modo = int(input('Qual modo de jogo você gostaria de executar?\nHumano x humano(1) humano x computador(2) computador x computador(3)\n:'))

while True:
    if modo == 1:
        jogador1 = int(input('FAÇA SUA JOGADA!\n1-PEDRA 2-PAPEL 3-TESOURA\n:'))
        jogador2 = int(input('FAÇA SUA JOGADA!\n1-PEDRA 2-PAPEL 3-TESOURA\n:'))
    elif modo == 2:
        jogador1 = int(input('FAÇA SUA JOGADA!\n1-PEDRA 2-PAPEL 3-TESOURA\n:'))
        jogador2 = random.choice([1, 2, 3])
        print('Computador escolhe\n:', jogador2)
    elif modo == 3:
        print('1-PEDRA 2-PAPEL 3-TESOURA')
        jogador1 = random.choice([1, 2, 3])
        jogador2 = random.choice([1, 2, 3])
        print('Computador1 escolhe\n:', jogador1)
        print('Computador2 escolhe\n:', jogador2)

    if (jogador1 == 1 and jogador2 == 1) or (jogador1 == 2 and jogador2 == 2) or (jogador1 == 3 and jogador2 == 3):
        print('EMPATOU')
    elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (jogador1 == 3 and jogador2 == 2):
        pont1 += 1
        print(resultado1)
    elif (jogador1 == 3 and jogador2 == 1) or (jogador1 == 1 and jogador2 == 2) or (jogador1 == 2 and jogador2 == 3):
        pont2 += 1
        print(resultado2)
    print('TABELA:')
    print('jogador1:', pont1, 'pontos')
    print('jogador2:', pont2, 'pontos')
    opção = str(input('DESEJA CONTINUAR JOGANDO?\n:'))
    if opção == ('sim' or 'SIM'):
        continue
    else:
        print('OBRIGADO POR JOGAR!')
        print('TABELA FINAL')
        print('jogador1:', pont1, 'pontos')
        print('jogador2:', pont2, 'pontos')
        print('game made by: Matheus Bernardi')
        break











