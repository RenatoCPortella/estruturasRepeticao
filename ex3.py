# while True:
#     nome = input('Digite um nome: ')
#     idade = int(input('Digite uma idade:: '))
#     sal = float(input('Digite um salario: '))
#     sexo = input('Digite F para feminino ou M para masculino: ').upper()
#     estcivil = input('Estado civil S, C, V ou D: ').upper()
#
#     if (len(nome) > 3) and (idade > 0 and idade < 150) and (sal > 0) and (sexo == 'M' or sexo == 'F') and \
#             (estcivil == 'S','C','V','D'):
#         print('certo')
#         break
#     else:
#         print('Voce digitou algo errado, tente novamente')

#ver depois


nome = ''
idade = 0
salario = 0
sexo = ''
estado_civil = ''

while len(nome)<=3:
  nome = input('Nome: (com mais de 3 letras)')

while idade < 0 or idade > 150 :
  idade = input('Idade:(entre 0 e 150) ')

while salario <= 0:
  salario = input('Salário: (maior que 0) ')

while sexo != 'f'  and sexo != 'm':
  sexo = input('Sexo: [m/f]')

while estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd':
  estado_civil = input('Estado Civil: [s/c/v/d]')