def opções_maquina():
    print("Bem-vindo à máquina de bebidas!")
    print('-'*20)
    print("ESCOLHA SUA BEBIDA:")
    print('-'*20)
    print(f'{"ID"}     {"Produto"}')
    print(f'1      Coca-Cola')
    print(f'2      Pepsi')
    print(f'3      Monster')
    print(f'4      Café')
    print(f'5      Redbull')
    print('-'*20)


def calcular_troco(valor_troco):
    denominacoes = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    resultado = []

    for denominacao in denominacoes:
        quantidade, valor_troco = divmod(round(valor_troco, 2), denominacao)
        if quantidade > 0:
            resultado.append([denominacao, int(quantidade)])
    print('-' * 10)
    print('TROCO')
    print('-' * 10)
    for v in resultado:
        if v[0] > 1:
            print(f'{v[1]} nota(s) de R${v[0]:.2f}')
        else:
            print(f'{v[1]} moeda(s) de R${v[0]:.2f}')


def pagamento_valor(ped, pag):
    if pagamento < maquina_vendas[pedido]['Preço']:
        print('DINHEIRO INSUFICIENTE!')
    else:
        troco = pagamento - maquina_vendas[pedido]['Preço']
        calcular_troco(troco)
        maquina_vendas[pedido]['Estoque'] -= 1


def pergunta():
    import time
    while True:
        resposta = str(input('Deseja continuar comprando? [S/N]\n')).upper()[0]
        if resposta in 'SN':
            break
    if resposta in 'N':
        print('OBRIGADO. VOLTE SEMPRE!')
        for i in range(0, 3):
            print('.')
            time.sleep(0.8)
        opções_maquina()


maquina_vendas = {1: {'Produto': 'Coca-Cola', 'Preço': 3.73, 'Estoque': 2},
                  2: {'Produto': 'Pepsi', 'Preço': 3.67, 'Estoque': 5},
                  3: {'Produto': 'Monster', 'Preço': 9.96, 'Estoque': 1},
                  4: {'Produto': 'Café', 'Preço': 1.25, 'Estoque': 100},
                  5: {'Produto': 'Redbull', 'Preço': 13.99, 'Estoque': 2}
                  }
opções_maquina()
while True:
    pedido = int(input('Qual Bebida você gostaria de comprar?(ID)'))
    if pedido > 5:
        print('ID INVALIDO!, Tente inserir um ID valido.')
    if pedido == 1:
        if maquina_vendas[pedido]['Estoque'] != 0:
            print(maquina_vendas[pedido]['Produto'])
            print(f'Preço: R${maquina_vendas[pedido]['Preço']} ')
            pagamento = float(input('Precisa de troco para quantos reais?'))
            pagamento_valor(pedido, pagamento)
            pergunta()
        else:
            print('Não temos esse produto no estoque')
            print('Tente outro ID')
    if pedido == 2:
        if maquina_vendas[pedido]['Estoque'] != 0:
            print(maquina_vendas[pedido]['Produto'])
            print(f'Preço: R${maquina_vendas[pedido]['Preço']} ')
            pagamento = float(input('Precisa de troco para quantos reais?'))
            pagamento_valor(pedido, pagamento)
            pergunta()
        else:
            print('Não temos esse produto no estoque')
            print('Tente outro ID')
    if pedido == 3:
        if maquina_vendas[pedido]['Estoque'] != 0:
            print(maquina_vendas[pedido]['Produto'])
            print(f'Preço: R${maquina_vendas[pedido]['Preço']} ')
            pagamento = float(input('Precisa de troco para quantos reais?'))
            pagamento_valor(pedido, pagamento)
            pergunta()
        else:
            print('Não temos esse produto no estoque')
            print('Tente outro ID')
    if pedido == 4:
        if maquina_vendas[pedido]['Estoque'] != 0:
            print(maquina_vendas[pedido]['Produto'])
            print(f'Preço: R${maquina_vendas[pedido]['Preço']} ')
            pagamento = float(input('Precisa de troco para quantos reais?'))
            pagamento_valor(pedido, pagamento)
            pergunta()
        else:
            print('Não temos esse produto no estoque')
            print('Tente outro ID')
    if pedido == 5:
        if maquina_vendas[pedido]['Estoque'] != 0:
            print(maquina_vendas[pedido]['Produto'])
            print(f'Preço: R${maquina_vendas[pedido]['Preço']} ')
            pagamento = float(input('Precisa de troco para quantos reais?'))
            pagamento_valor(pedido, pagamento)
            pergunta()
        else:
            print('Não temos esse produto no estoque')
            print('Tente outro ID')





















