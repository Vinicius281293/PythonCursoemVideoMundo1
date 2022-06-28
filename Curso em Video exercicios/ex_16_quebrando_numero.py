"""
---------------- Exercício 16 ----------------

CURSO
EM 
VÍDEO

 -------- ENUNCIADO ---------
Crie um programa que leia um número Real
Qualquer pelo teclado e mostre na tela a sua
função inteira.

"""
import math
numero = float(input('Digite um número '))
print(' O valor digitado foi {} e sua porção inteira foi {}'.format(numero, math.trunc(numero)))

from math import trunc
numero1 = float(input('Digite um número '))
print(' O valor digitado foi {} e sua porção inteira foi {}'.format(numero1, trunc(numero1)))