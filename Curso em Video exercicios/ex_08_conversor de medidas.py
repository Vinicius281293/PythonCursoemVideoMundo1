# -------------------- Conversor medidas --------------
#EXERCICIO 08 
#CURSO EM VÍDEO 

#Escreva um valor em metros que seja convertido em centímetros e milímetros 

medida = float(input('informe a distância em metros: '))
centimetros = medida * 100
milimetros  = medida * 1000
print('A média de de {}m  corresponde a {} centímetros e {} milímetros'.format(medida, centimetros, milimetros))