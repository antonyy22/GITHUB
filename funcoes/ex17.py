def defeituoso(lista):
    contador =0
    for n in lista:
        if n > 0:
            contador+=1

        return contador
    print(contador)    
def main ():
    listas= [2,45,6,7,2,-2,-4,-15,-54,64,-43]
    defeituoso(listas)



main()