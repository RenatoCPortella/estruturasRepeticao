print('Cardápio: \n'
      'Especificação   Código  Preço\n'
      'Cachorro Quente 100     R$ 1,20\n'
      'Bauru Simples   101     R$ 1,30\n'
      'Bauru com ovo   102     R$ 1,50\n'
      'Hambúrguer      103     R$ 1,20\n'
      'Cheeseburguer   104     R$ 1,30\n'
      'Refrigerante    105     R$ 1,00\n')
esc = 'S'
lista = []

while esc != 'N':
    pedido = int(input('Digite o código do produto desejado: '))
    qtd = int(input('Digite a quantidade desejada: '))
    if pedido == 100:
        v = 1.20 * qtd
        lista.append(v)
    elif pedido == 101:
        v = 1.30 * qtd
        lista.append(v)
    elif pedido == 102:
        v = 1.50 * qtd
        lista.append(v)
    elif pedido == 103:
        v = 1.20 * qtd
        lista.append(v)
    elif pedido == 104:
        v = 1.30 * qtd
        lista.append(v)
    elif pedido == 105:
        v = 1.00 * qtd
        lista.append(v)
    else:
        print('Digite o código correspondente ao produto desejado!')

    esc = input('deseja continuar? "S" para SIM e "N" para NÃO: ').upper()

vt = sum(lista)
print(f'O valor total do seu pedido é de: R${vt}')
