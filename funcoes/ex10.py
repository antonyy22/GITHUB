def pares(lista_numeros):
    lista_pares = [ ]

    for numero in lista_numeros:
        if numero % 2== 0:
            lista_pares.append(numero)
    return lista_pares

def main ():
    lista_numeros= [3,5,7,3,2,7,8,4,67]
    lista_final= pares(lista_numeros)
    for n in lista_final:
        print (n, end=' ')
    print ()

main()