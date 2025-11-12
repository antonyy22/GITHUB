def gera_lista(lista):
    for i in range(5):
        fruta=input('Insire uma fruta -> ')
        lista.append(fruta)
    return lista


def escrever_frutas(lista):
    with open ('frutas.txt', 'w') as arquivos:
        for fruta in lista:
            arquivos.write(fruta+ '\n')

        print ('Arquivo gerado ')


def main ():
    lista= []
    lista= gera_lista(lista)
    escrever_frutas(lista)


main()