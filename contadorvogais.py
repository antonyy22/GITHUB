palavra= input ("Informe uma paçvara -> ")
contador= 0
vogais = 0
while contador < len(palavra):
    if palavra [contador] =="a":
        vogais+=1 
    elif palavra [contador] =="e":
        vogais+=1
    elif palavra [contador] =="i":
        vogais+=1
    elif palavra [contador] =="o":
        vogais+=1
    elif palavra [contador] =="u":
        vogais+=1
    contador +=1

print ("A palavra", palavra, "tem", vogais, "vogais")