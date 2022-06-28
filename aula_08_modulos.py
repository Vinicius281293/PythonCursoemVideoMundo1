#CURSO
# EM 
# VÍDEO

'''
---------- Aula 08 - Utilizando Módulos -------------
Bibliotecas de código - É o conceito que adiciona novas ferramentas no uso da programação, com novas funções,importando uma Biblioteca.
exemplo: import math  (biblioteca para cálculos)

'''
#import math

# Ao importar uma biblioteca com import, (todo o conteúdo) da biblioteca é baixado.

# Quando precisamos importar algo (específico) dentro da biblioteca usamos o 
#from math import 

# Funcionalidades Math
"""
ceil - Arredondamento para cima 
floor - Arredondamento para baixo
trunc - Elimina da vírgula para frente
pow - potência
sqrt - Raiz Quadradra
factorial


"""


import math
numero = int(input('Digite um número: ' ))
raiz = math.sqrt(numero)
print(f'A raiz de {numero} é igual a {raiz:.2f}')
print('A raiz de {} é igual a {}'.format(numero, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(numero, math.floor(raiz)))

from math import sqrt, floor
numero = int(input('Digite um número: '))
raiz = sqrt (numero)
print('A raiz de {} é igual a {}'.format(numero, floor(raiz)))
