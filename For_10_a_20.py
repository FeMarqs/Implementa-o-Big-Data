# -*- coding: utf-8 -*-
"""Cópia de Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13eZhNO0Bv6WYWuMT7R2VXAOtf74D_i4Y
"""

if idade >= 0 and idade < 16:
  print('Você não pode apenas votar')

elif idade >= 16 and idade < 18:
  print('Você pode apenas votar')

elif idade >=18 and idade < 21:
  print('Você pod votar e tem maioridade penal')

elif idade >= 21 and idade < 120:
  print('Você pode votar, tem maioridade penal e civil')

else:
  print('Idade errada')

#Reajuste Salarial

salario = float(input('Salário atual R$: '))


if salario < 1500:
  print(f'Seu salário com reajuste de 25% é: {(salario * 0.25) + salario} ')
elif salario <= 1500 and salario < 1999.99:
  print(f'Seu salário com reajuste de 20% é de: {(salario * 0.20) + salario}')
elif salario >= 2000 and salario < 1999.99:
  print(f'Seu salário com reajuste de 15% é de: {(salario * 0.15) + salario}')
elif salario >= 3000 and salario < 4999.99:
  print(f'Seu salário com reajuste de 10% é de: {(salario * 0.10) + salario}')
elif salario > 5000:
  print(f'O salário com o reajuste de 5% é R$: {(salario * 0.05) + salario} ')

# For de 10 a 20

for i in range (11):
  print(i + 10)

# For de 10 a 20

for i in range (11):
  print(10 - i)

nome = 'jean'
# duas maneiras diferentes de fazer o mesmo for

#for i in range(4):
  print(nome[i])

for i in range(len(nome)):
  print(nome [i])

for i in nome:
    print (i)

# FORCA

secreta = 'banana'

for i in range(5):
  letra = input('digite uma letra: ')

  resultado = ''
  for i in secreta:
    if letra == i:
      resultado += i
    else:
      resultado += '-'
  print(resultado)