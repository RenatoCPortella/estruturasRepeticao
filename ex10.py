# num1 = int(input('Digite um numero inteiro: '))
# num2 = int(input('Digite outro numero inteiro: '))
# if num1 > num2:
#     maior = num1
#     menor = num2
# else:
#     maior = num2
#     menor = num1
# maior -= 1
# while menor < maior:
#     menor += 1
#     print(menor)
# print()


n1 = int(input('Infome um numero inteiro: '))
n2 = int(input('Infome outro numero inteiro: '))
soma = 0
if n1 > n2:
    for a in range(n2 + 1, n1):
        print(a)
        soma = soma + a

elif n1 < n2:
    for a in range(n1 + 1, n2):
        print(a)
        soma = soma + a
else:
    print('Os numeros são iguais.')
print(f'A soma dos numeros foi de {soma}')
