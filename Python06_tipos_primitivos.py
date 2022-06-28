# Aula 06 - Tipos Primitivos 
# CURSO 
# EM 
# VÍDEO

# Variáveis são pequenos espaços na memória para guardar um valor 


#  ------------  INPUT PARTE 2 ---------------
#  O input é caracterizado como String
# para adicionar números e somar o valores é necessário adicionar int ou float, para alterar tipo numérico.

num1 = int(input('Digite um número: ' ))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
print('A soma é ', soma)


#  --------------- Tipos Primitivos ---------------
# Inteiros int = 7, -4, 0, 9875
# flutuante float, real = 4.5, 0.076, -15.223, 7.0
# booleano bol: True, False 
# string str: ' Olá ', ' 75 ', ' '

# Print com .format 
print('A soma entre {} + {} = {} '.format(num1,num2, soma))
# F String
print(f'A soma entre {num1} + {num2} = {soma}')

# ----------------- TYPOS EM PYTHON ------------
# Para ver o tipo de dados nó temos que utilizar a função TYPE

n1 = input('Digite um número: ' )
print(type(n1))
# ---------  Explicação ----------
#Quando nós usamos a função input, mesmo sendo número o tipo é < class ' str ' >
# lista de tipos
l1 = 9
l2 = 'Pedro '
l3 = '5'
l4 = True
l5 = 7.0
print(type(l1), l1)
print(type(l2), l2)
print(type(l3), l3)  # L3 é string, str  pois o número 5 está entre aspas '5' 
print(type(l4), l4)
print(type(l5), l5)

# OUTROS TIPOS
algo = input('Digite alguma coisa: ')
print(algo.isnumeric())
# isnumeric é função que pergunta se pode ser convertido para o tipo int
print(algo.isalpha())
# Se é letra, alfabético
print(algo.isalnum())
# Se é alfanumérico
print(algo.isupper())
# Se é maiúscula