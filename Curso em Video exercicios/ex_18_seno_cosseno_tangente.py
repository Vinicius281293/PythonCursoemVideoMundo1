'''
Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

'''
# from math import radians, sin, cos, tan
#Quando usar from, lembrar de rirar math e deixar só o arquivo impotado:
#seno = sin(radians(angulo))
import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
print(f'Ângulo de {angulo} tem o SENO de {seno:.2f}')
cosseno = math.cos(math.radians(angulo))
print(f'O ângulo de {angulo} tem o Cosseno de {cosseno:.2f}')
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem a tangente de {tangente:.2f}')