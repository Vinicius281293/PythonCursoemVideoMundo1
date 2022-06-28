#ex_03_Uninter
#Define o valor pelas dimensões
def valor():

  while True:
      try:
        altura = float(input('Digite a altura em centímetros: '))
        comprimento = float(input('Digite o comprimento em centímetros: '))
        largura = float(input('Digite a largura em centímetros: '))         
        dimensão = float(altura*comprimento*largura)
        print('A dimensão da caixa é de', dimensão, 'centimetros³.')
        
      
        if dimensão <= 1000:
          return 10.00
          
          
                
        elif dimensão in range (1001, 10000):
          return 20.00
          
          
                
        elif dimensão in range (10001, 30000):
          return 30.00
          
          
                
        elif dimensão in range (30001, 100000):
          return 50.00
          
          

        else:
          print('Desculpe, não trabalhamos com objetos deste tamanho.')
          continue

      except ValueError:
          print('Digite um número inteiro!')        
          continue


#Define o multiplicador pelo peso
def multiplicador():
  while (True):
          
          try:
            peso = float(input('Digite o peso (em kg): '))          
          
            
            if peso <= 0.1:
             return 1.0
             print('x1')
              
            elif (peso>0.11) and (peso<=1):
             return 1.5
             print('x1.5')

            elif (peso>1.10) and (peso<=10):
             return 2.0
             print('x2')

            elif (peso>10.1) and (peso<=30):
              return 3.0
              print('x3')            
            elif peso>30:
              print('Desculpe, não trabalhamos com objetos deste peso.')         
              continue           

          except ValueError:
           print('Você digitou um peso com valor não numérico!')
           continue     

          






#Define multiplicador pela distância
def distancia():
 while True:
        try:
          rota = str(input('Digite o código da rota desejada:\nRS - De Rio de Janeiro até São Paulo\nSR - De São Paulo até Rio de Janeiro \nBS - De Brasília até São Paulo\nSB - De São Paulo até Brasília\nBR - De Brasília até Rio de Janeiro\nRB - Rio de Janeiro até Brasília11'))
          
          if rota.upper() == "RS":
            return 1  

          elif rota.upper() == "SR":
            return 1

          elif rota.upper() == "BS":
            return 1.2

          elif rota.upper() == "SB":
            return 1.2

          elif rota.upper() =="BR":
            return 1.5

          elif rota.upper() == "RB":
            return 1.5
                      
                                      
          else:
            print('Você digitou uma rota que não existe, Digite Novamente!1')
            continue

        except ValueError:
          print('Digite um código válido!')
          continue    





#Define  o valor final
print('Bem vindos à Companhia de Logística Vinícius Fernandes Rodrigues  SA RU: 3837437')
print('Para simular o valor do transporte, insira os dados do objeto.')  

valor = valor()
multiplicador = multiplicador()
distancia = distancia()
print('Valor em função das dimensões:R$ {:.2f}' .format(valor))
print('Valor multiplicado por', multiplicador, 'vez(es), em função do peso')
print('Valor multiplicado por', distancia, 'vez(es), em função da distância')

valorFinal = valor*multiplicador *distancia

print('O valor do transporte ficará em R$ {:.2f}' .format(valorFinal),'.')

