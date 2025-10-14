a= (1,1,5,5,4,7,9,25,75,2,7,86,25,75)
numeros= []
for i in a:
    if i not in numeros:
        numeros.append(i)

tuplafinal= tuple(numeros)
print (*tuplafinal)
print(type(tuplafinal)) 