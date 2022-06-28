#import emoji
#print(emoji.emojize("Olá mundo : sunglasses: " , use_aliases = True))

# Inverter String 
#msg = " Mario "
#invertida = msg [::-1]
#print(invertida)

#def inverter (num):
#    msg = str(num)
#    return int(msg[::-1])
#print(inverter(1235))
#valor = int(input ("Digite um valor: ")
#print(inverter)

def ehpalindromo(msg):
    invertido = msg[:: -1]
    if msg == invertido:
        return True 
    else:
        return False

texto = input("Digite uma palavra:")
if ehpalindromo (texto):
    print("palindromo")
else:
    ("Não é palindromo ")
   
def potencia(base, expoente):
    resp = 1
    for i in range (expoente):
        resp *= base
    return resp
print(potencia(3,2 ))

def compressao(d1, d2, d3):
    return d1 * 100  + d2 * 10 + d3
    

def texto (n1, n2, n3):
   num = str(n1) + str(n2) + str(n3)
   return int(num)
print(texto(10,20,30))
   