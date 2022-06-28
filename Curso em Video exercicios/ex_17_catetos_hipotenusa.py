'''
17 Exercício - Cateto e Hipotenusa
Faça um programa que leia o comprimento
do cateto oposto e do cateto adjacente de um triângulo retângulo e mostre o comprimento.

'''
catetoOposto = float(input('Comprimento do Cateto Oposto: '))
catetoAdjacente = float(input('Comprimento do Cateto Adjacente: '))
# Hipotenusa é a raiz quadrada da soma dos quadrados dos catetos
hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')

#import math 
from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do cateto Adjacente: '))
#hi = math.hypot(co, ca)
hi = hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')