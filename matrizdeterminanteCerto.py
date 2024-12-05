# -*- coding: utf-8 -*-
"""MatrizDeterminante.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kTSIAXVnfzmoWT4y4i5Ab9d6z4uanr73
"""

import random as r

a = [[r.randint(1,10),r.randint(1,10),r.randint(1,10)],[r.randint(1,10),r.randint(1,10),r.randint(1,10)],[r.randint(1,10),r.randint(1,10),r.randint(1,10)]]

b = [[r.randint(1,10),r.randint(1,10),r.randint(1,10)],[r.randint(1,10),r.randint(1,10),r.randint(1,10)],[r.randint(1,10),r.randint(1,10),r.randint(1,10)]]
print(a)
print(b)

multiplicaA = (a[0][0] * a[1][1] * a[2][2]) + (a[0][1] * a[1][2] * a[2][0]) + (a[0][2] * a[1][0] * a[2][1])
print(multiplicaA)

multiplicaB = (a[0][2] * a[1][1] * a[2][0]) - (a[0][0] * a[1][2] * a[2][1]) - (a[0][1] * a[1][0] * a[2][2])
print(multiplicaB)

determinante = multiplicaA - multiplicaB
print('A determinante da Matriz é: ', determinante)