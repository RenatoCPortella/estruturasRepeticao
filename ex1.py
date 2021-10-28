# nota = int(input('Digite uma nota de 0 a 10'))
#
# while nota < 0 or nota > 10:
#     print('Digite uma nota valida!')
#     break
# print('Essa é uma nota valida')

nota = -1

while nota < 0 or nota > 10:
    nota = int(input("Informe a nota: "))

    if nota < 0 or nota > 10:
        print("Valor inválido")
