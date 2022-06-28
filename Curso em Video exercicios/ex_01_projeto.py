# Exercício 01 Uninter
print('Bem vindo a Loja do Vinicius Fernandes Rodrigues Ru3837437')
valor = float(input('Informe o valor do produto R$ '))
quantidade = int(input('Informe a quantidade do produto: '))
semDesconto = valor * quantidade

if 0 <= quantidade < 10:
    print('O Produto custa R${:.2f} sem desconto'.format(semDesconto))

elif 10 <= quantidade < 100:
    print('O Produto custa R${:.2f} sem desconto'.format(semDesconto))
    print('O Produto custa R${:.2f} com desconto de 5%'.format(semDesconto - (semDesconto * 5 / 100)))

elif 100 <= quantidade < 1000:
    print('O Produto custa R${:.2f} sem desconto'.format(semDesconto))
    print('O Produto custa R${:.2f} com desconto de 10%'.format(semDesconto - (semDesconto * 10 / 100)))
# Os dois valores são informados, o valor como desconto e sem desconto.
else:
    print('O Produto custa R${:.2f} sem desconto'.format(semDesconto))
    print('O Produto custa R${:.2f} com desconto de 15%'.format(semDesconto - (semDesconto * 15 / 100)))
# Optei por colocar o cálculo completo no código  em vez de fazer direto o resultado das porcentagens.
