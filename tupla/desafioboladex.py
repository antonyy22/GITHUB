cordenas= []
cont = 0

for linha in range(3):
    temp= []
    for coluna in range (2):
        temp.append(cont + 1)
        cont +=1

    cordenas.append(tuple(temp))
cordenas=tuple (cordenas)
print (cordenas, '\n')
