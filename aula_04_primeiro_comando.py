#Aula 04 -- Primeiros comandos em Python
# CURSO
# EM
# VÍDEO

# ------------ Delimitadores -------------
# Sempre que estamos tratando de texto
# o python pussui delimitadores.
# 'Aspas Simples ', "Aspas Duplas"
# também usamos parênteses
#          (' Olá, mundo ') 

# ---------------- FUNÇÃO -------------
# Print é a função, Escreva:
 # Escreva na tela, exiba na tela.
print ('olá mundo! ')

#-------------------- NÚMEROS-------------------------
#  5 e 4: São números, para fazer cálculos
# não utilizamos aspas. Apenas () parênteses.
print(5 + 4)

# ------------ Números com ASPAS -----------
# Ao utilizamos números com aspas simples o número deixa de ser número e passa a ser texto (string).
print('5' + '4')
# Em vez de somar ele apenas junta os números, sendo o valor 54.

# ---------- Números + Textos ----------
# Não é possível usar o operador de adição
# Com textos e números, pois ocorre um erro.

 # ---------------- Erro -------------
#            print('Olá mundo! ' + 5)
 #------------------ Erro -----------
 
# Erro, Não é possível concatenar, números com String.
# Obs: Concatenar é o mesmo que juntar dois textos(duas strings)
 
 # ---------------- Solução com vírgula ----
print(' olá, mundo! ', 5)

# --------------- Variaveis ---------------
# Toda variável é um objeto
#toda Variável pode receber um valor
#variável / atribuição / valor.
#nome           =                 'Vinicius'
#idade           =                  '28 '
#peso            =                   '60 '

# REGRAS DAS VARIÁVEIS
# Não utilizar caracteres especiais ex: @,#,$
# Não utilizar espaços  ex: nome aluno
# Não começar com números ex: 1aluno
# Não usar palavras reservadas ex: print, input
# Ex: input = input (ERROR)
# É possível utilizar _ underline ex: nome_aluno
# É possível usar números no final ex: aluno1
# É possível começar com underline ex: _aluno
# Camel Case ex: nomeAluno
# snake_case ex: nome_aluno
# Utilizar nomes de Variáveis de fácil identificação
# Evitar variaveis ex: n = que possam ser de fácil esquecimento.


nome = 'Vinicius '
idade = 28
peso = 60
print(nome, idade, peso)

# ----------------- Função Leia (Input) ---------------
# A função leia cria interação com o usuário fazendo que o usuário digite seus dados.
nome = input ('Qual seu nome: ' )
idade = input ( 'Qual sua idade: ')
peso = input ('Qual seu peso: ' )
print(nome, idade, peso)

#Desafio 1 Crie um script que leia o nome de uma pessoa e uma mensagem de boa vindas.

nome = input(' Digite seu nome: ')
print('Bem vindo! ', nome)

#Desafio 2 - Crie um script que leia o dia, mês e ano de uma pessoa e mostre formatado.

nome = input('Digite seu nome: ' )
dia = input('Informe o dia que nasceu: ')
mes = input ('Informe o mês que nasceu: ')
ano = input('Informe o ano em que nasceu: ')
print('{}, nasceu no dia {} de {} de {}'.format(nome, dia, mes, ano))

# Desafio 3 - Crie um script que pegue dois números e some entre eles
num1 = int(input('Digite um número: ' ))
num2 = int(input('Digite outro número: '))
print (num1 + num2)
print(' A soma é',  num1 + num2)
