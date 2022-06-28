#Exercício Python 006  - Dobro, triplo, raiz
numero = int(input("Digite um número: "))
dobro =  numero * 2
triplo = numero * 3 # terça parte / por 3  ---- modelo 1 -----
raizQ = numero ** (1/2) # ordem de procedência ------- modelo 1 -----
print("O dobro de  {} vale {}.".format(numero, dobro)) # ---- modelo 1  ------
print("O dobro de {} vale {}".format(numero, (numero*2)))
print("O triplo do {} vale {}. \n A raiz quadradra de {} é igual a {:.2f}".format(numero, triplo, numero, raizQ))
#---- sem variável ------ print(' O  Triplo do {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}'.format(numero,(numero*3), numero, (numero**(1/2))))
# ----- sem Variável ---- print(' O  Triplo do {} vale {}. \n A raiz quadrada de {} é igual a {:.2f}'.format(numero,(numero*3), numero, pow(numero, (1/2))))
