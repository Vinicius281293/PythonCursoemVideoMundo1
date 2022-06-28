# ------------- CONVERSOR DE MOEDAS ----------
# CURSO
# EM
# VÍDEO
# -------------- EXERCÍCIO 09 ---------------------
# Crie um programa que leia quanto dinheiro a pessoa tem na carteira e converta para dólares.

real = float(input('Digite um valor em R$'))
dollar = real/ 5.13
euro = real / 5.41
print('Com R${:.2f} reais, você pode comprar US${:.2f} dólares'.format(real, dollar))

print(f'Com R${real:.2f} reais, você pode comprar US${dollar:.2f} dólares')

print(f'Com R${real:.2f} reais, você pode comprar  € {euro:.2f} euros')