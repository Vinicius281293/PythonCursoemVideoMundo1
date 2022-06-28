#ex_04_uninter
lista_pecas = []
def cadastrar_peca(codigo):
  print('Você selecionou a opção de Cadastrar Peça')
  print('O código da peça é: {:0>3}'.format(codigo))
  nome = input('Entre com o nome da peça:') #Onde Cadastramos as peças com o nome,por fabricante  e o valor
  fabricante = input('Entre com o fabricante da peça:')
  valor = float(input('Entre com o valor R$ da peça:'))
  dicionario_pecas = {'codigo'   : codigo,
                         'nome' : nome,
                         'fabricante': fabricante,
                         'valor': valor}
  lista_pecas.append(dicionario_pecas.copy())
def consultar_peca():
  while True:
# Aqui onde consultamos a peça cadastrada 
    try:
      print('Você Selecionou a Opção de Consultar Peças')
      consultarp = int(input('Entre com a opção desejada\n1- Consultar Todas as Peças\n2- Consultar Peças por Código\n3- Consultar Peças por Fabricante\n4- Retornar\n-->'))
      if consultarp == 1:
        print('-' * 20)
        for pecas in lista_pecas:
            for key, value in pecas.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif consultarp == 2:
        print('Você Selecionou a Opção Peças por Código')
        entrada = int(input('Digite o Código: '))
        print('-' * 20)
        for pecas in lista_pecas:
          if(pecas['codigo'] == entrada):
            for key, value in pecas.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif consultarp == 3:
        print('Você Selecionou a Opção Peças por Fabricante')
        entrada = input('Digite o Fabricante: ')
        print('-' * 20)
        for pecas in lista_pecas:
          if(pecas['fabricante'] == entrada):
            for key, value in pecas.items():
              print('{} : {}'.format(key,value))
            print('-' * 20)
      elif consultarp == 4:
        break
      else:
        print('Por favor digite somente o que pede') # Caso a opção esteja incorreta, número inexistente.
        continue
    except ValueError:
      print('O numero que você digitou não existe, digite novamente!')
      continue
# Removendo peças 
def remover_peca():
    print('Você Selecionou o Remover Peça')
    entrada = int(input('Digite o Código da peça que irá remover: '))
    for pecas in lista_pecas:
      if(pecas['codigo'] == entrada):
        lista_pecas.remove(pecas)
    else:
      print('Você removeu o código.')
print('Bem-vindo ao Controle de Estoque da Bicicletaria do Vinicus Fernandes Rodrigues 3837437')
registro_pecas = 0
while True:
    try:
      opcao = int(input('Digite a opção desejada:\n1- Cadastrar Pecas\n2- Consultar Pecas\n3- Remover Pecas\n4- Sair\n-->'))
      if opcao == 1: 
        registro_pecas = registro_pecas + 1
        cadastrar_peca(registro_pecas)
      elif opcao == 2:
        consultar_peca()
      elif opcao == 3:
        remover_peca()
      elif opcao == 4:
        print('Programa finalizado')
        break
      else:
        print('Digite somente uma das opções do MENU')
        continue
    except ValueError:
        print('O numero que você digitou não existe, digite novamente!')
