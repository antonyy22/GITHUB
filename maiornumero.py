numero=1 
maiornumero= 0

while numero != 0:
    numero= int (input("informe um numero - > "))

    if numero > maiornumero:
        maiornumero=numero

    else:
        maiornumero= maiornumero

print ("O maior numero e ", maiornumero)
