def ler_lista(lista):
    for i in lista:
        print(i, end= ' | ')


def obtem_erro(lista):
    try:
        ler_lista(lista)
    except Exception as erro:
        print('Erro encontrado', erro)

def main():
    lista_fake=1000
    lista= [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    obtem_erro(lista_fake)



main()