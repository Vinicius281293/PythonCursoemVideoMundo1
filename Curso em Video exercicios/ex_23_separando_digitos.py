'''

Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.

'''
nome = input('Digite seu nome completo: ').strip()
print('Seu nome em maiúsculo é',nome.upper())
print('Seu nome em minúsculo é',nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print(' ')
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras '.format(separa[0], len(separa[0])))


