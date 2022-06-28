#ex_02 Uninter
#Cardápio de Lanches e Bebidas
print('Bem Vindo a Lanchonete do Vinicius Fernandes Rodrigues RU3837437 ')

print ('Faça seu pedido, Seguindo o Cardápio :')

print('\033[34m_\033[m' * 45)

print(f'\033[33m{"CARDAPIO":^45}\033[m')

print('\033[34m_\033[m' * 45)

print ('\033| Código |     Descrição         | Valor| \033')

print ('\033|  100   | Cachorro Quente       | 9,00 |\033')

print ('\033|  101   | Cachorro Quente Duplo | 11,00|\033')

print ('\033|  102   | X-Egg                 | 12,00|\033')

print ('\033|  103   | X-Salada              | 12,00|\033')

print ('\033|  104   | X-Bacon               | 14,00|\033')

print ('\033|  105   | X-Tudo                | 17,00|\033')

print ('\033|  200   | Refrigerante Lata     | 5,00 |\033')

print ('\033|  201   | Chá Gelado            | 4,00 |\033')



#Valor unitário dos itens
cachorroQuente = 9

cachorroQuenteDuplo = 11

xEgg = 12

xSalada = 12

xBacon = 14

xTudo = 17

refrigerante = 5

chaGelado = 4





total=0

opcao = int(input(' Digite 1 para começar o seu pedido\n'))



while (opcao != 1):#Enquanto não for 1 o sistema não vai começar.
   

    print('Opção Inválida! Digite o código novamente:')

    opcao = int(input('Digite 1 para começar o seu pedido'))

      



while (opcao == 1): #Repetir enquanto opção digitada seja igual a 1  

    codigo = int(input('Digite o código do produto ou 2 para fechar o pedido:')) #Escolha do item pelo código do cardápio.

    if codigo == 2:

        break

        exit()

    elif codigo == 100:

        total=total+(cachorroQuente)

        print('Você pediu um Cachorro Quente no valor de R$ {:.2f}'.format(cachorroQuente))

        continuar = int(input("Deseja pedir mais alguma coisa?\n1 - SIM\n2 - NÃO\nR:"))

        

        

    elif codigo == 101:

        total=total+(cachorroQuenteDuplo)

        print('Você pediu um Cachorro Quente Duplo no valor de R$ {:.2f}'.format(cachorroQuenteDuplo))

        continuar = int(input("Deseja pedir mais alguma coisa?\n1 - SIM\n2 - NÃO\nR:"))

        if continuar == 2:

            break

    elif codigo == 102:

        total=total+(xEgg)

        print('Você pediu um X-Egg no valor de R$ {:.2f}'.format(xEgg))

        continuar = int(input("Deseja pedir mais alguma coisa?\n1 - SIM\n2 - NÃO\nR:"))

        if continuar == 2:

            break

    elif codigo == 103:

        total=total+(xSalada)

        print('Você pediu um X-Salada no valor de R$ {:.2f}'.format(xSalada))

        continuar = int(input("Deseja pedir mais alguma coisa?\n1 - SIM\n2 - NÃO\nR:"))

        if continuar == 2:

            break

    elif codigo == 104:

        total=total+(xBacon)

        print('Você pediu um X-Bacon no valor de R$ {:.2f}'.format(xBacon))

        continuar = int(input("Deseja pedir mais alguma coisa?\n1 - SIM\n2 - NÃO\nR:"))

        if continuar == 2:

            break

    elif codigo == 105:

        total=total+(xTudo)

        print('Você pediu um X-Tudo no valor de R$ {:.2f}'.format(xTudo))

        continuar = int(input("Deseja pedir mais alguma coisa?\n1 - SIM\n2 - NÃO\nR:"))

        if continuar == 2:

            break

    elif codigo == 200:

        total=total+(refrigerante)

        print('Você pediu um Refrigerante Lata no valor de R$ {:.2f}'.format(refrigerante))

        continuar = int(input("Deseja pedir mais alguma coisa?\n1 - SIM\n2 - NÃO\nR:"))

        if continuar == 2:

            break

    elif codigo == 201:

        total=total+(chaGelado)

        print('Você pediu um Chá Gelado no valor de R$ {:.2f}'.format(chaGelado))

        continuar = int(input("Deseja pedir mais alguma coisa?\n1 - SIM\n2 - NÃO\nR:"))

        if continuar == 2:

            break

        

    elif codigo == 2:  #Código para encerrar o loop

        break

           

    else: #Mensagem de erro, caso o código estiver errado 
        print('Opção Inválida! Digite o código novamente:')

        continue

    

valorFinal = "{:.2f}".format(total)

print('O total a ser pago é: R$', (valorFinal))

print("Obrigado pelo seu pedido!")

