# -*- coding: utf-8 -*-
"""Matriz2Aleatoria.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pwzEq-NFcNVgs2SHhMK2tznHvIpQqbo6
"""



"""Matrizes no Python - revisão

Crie um programa para gerar duas matrizes quadrada aleatórias (A e B), no intervalo [1,10], de mesma ordem, a qual deve ser de números aletórios. Ao fim, o programa deve calcular e imprimir a soma entre os elementos de A que estão abaixo da diagonal principal com os elementos de que estão acima da diagonal principal
"""

import random as r

a = [[r.randint(1,10),r.randint(1,10),r.randint(1,10)],[r.randint(1,10),r.randint(1,10),r.randint(1,10)],[r.randint(1,10),r.randint(1,10),r.randint(1,10)]]

b = [[r.randint(1,10),r.randint(1,10),r.randint(1,10)],[r.randint(1,10),r.randint(1,10),r.randint(1,10)],[r.randint(1,10),r.randint(1,10),r.randint(1,10)]]
print(a)
print(b)

somaA = a[0][1] + a[0][2] + a[1][2]
print(somaA)
somaB = b[1][0] + b[2][0] + b[2][1]
print(somaB)

print('O resultado é:' , somaA + somaB)