frase= str (input("Digite sua frase -> "))
contador=0
for letra in frase:
    if letra.isupper ():
        contador +=1
print ("A quantidade de letras maiusculas é", contador)