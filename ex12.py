num = int(input('Digite um número de 1 a 10: '))

if (num > 0) and (num < 11):
    for i in range(1, 11):
        mult = num * i
        print(f'{num} X {i} = {mult}')

else:
    print('Digite um número válido')