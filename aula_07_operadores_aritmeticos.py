#CURSO
#EM
#VÍDEO
#Aula 07  - Operadores Aritméticos 

# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência 
# // divisão inteira 
# % mod, resto da divisão 

# 5 + 2 == 7
# 5 - 2 == 3
# 5 * 2 == 10
# 5 / 2 == 2.5
# 5 ** 2 == 25
# 5 // 2 == 2
# 5 % 2 == 1

# == Sinal de Igualdade
# = Sinal de atribuição 

#ORDEM 
#DE 
# PROCEDÊNCIA

# 1° Parênteses ()
# 2° ** Potência
# 3° * adição, / divisão, // divisão inteira, % módulo
# 4° + adição, - subtração

# Exemplos
# -------------- CONTA NÚMERO 1 ---------------
# Ordem de procedência
# 3*2+5 = 11
conta1 = 5 + 3 * 2
print(conta1)

# ------------ CONTA NÚMERO 2 ------------
conta2 = 3*5+4**2
print(conta2)
#ordem de procedência 4**2 + 3*5 

# --------------- CONTA NÚMERO 3 -----------
conta3 = 3*(5+4)**2
print(conta3)
# ordem de procedência (5+4)**4*3

# ------------  CONTA NÚMERO 4  -------------
# Função interna potência com pow
potencia = pow(4,3)
print(potencia)

# ---------------- CONTA NÚMERO 5 -------------------
# Para calcular raizQ faça elevado a (1/2)
raizQ = 81**(1/2)
print(raizQ)
# -------------------- CONTA NÚMERO 6 ----------
# Para Calcular a raizCúbica faça elevado a (1/3)
raizCubica = 10 ** (1/3)
print(raizCubica)

# exemplos aleatórios
oi = 'oi' * 10
print(oi)
# print
print('olá mundo! ' * 5)

# ----------------------- EXERCÍCIO 01-----------------
nome = input('Digite seu nome: ' )
print('Prazer em te conhecer {:=^10} '.format(nome))

# É possível estabelecer a quantidade de caracteres {:20} 
# É possível alinhar a direita usando o sinal de maior {:>20}
# É possível alinhar a esquerda usando sinal de menor {:<20}
# É possível usar o acento circunflexo para centralizar {:^20}
# É possível usar o sinal de igualdade {:=^20}

# ----------------- EXERCÍCIO 02 --------------
# É possível fazer cálculos na função Print, não sendo necessário criar outra Variável.
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro numero: '))
print('A soma vale {}'.format(numero1 + numero2))
# --------------------- EXERCÍCIO 3 -------------------
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
soma = numero1 + numero2
multi = numero1 * numero2
divi = numero1 + numero2
divInteira = numero1 // numero2
potencia = numero1 ** numero2
print(f'A soma é {soma},  A multiplicação vale  {multi},  A divisão é {divi},  A divisão inteira é {divInteira}, e a potência é {potencia:.2f}')
# É possível limitar o número de casas decimais com :.2f, "float"
# print com end
print('A  soma é  {}, o produto é {}, e a divisão é {}'. format(soma, multi, divi), end= ' ')
print('A divisão inteira é {} potência é {2.:f}'.format(divInteira, potencia))
# No caso de utilizarmos dois prints e evitar que as duas linhas sejam quebradas, usamos o end = ' '
# Para quebrar a linha usamos o \n, Nova linha
