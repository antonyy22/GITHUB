import os       


def remover_arquivo(nome_arquivo):
    try:
        os.remove(nome_arquivo)
        print('arquivo apagado ')

    except FileNotFoundError:
        print('Arquivo nao existe ou ja foi apagado')


def main ():
    remover_arquivo(input("qual arquivo deseja apagar -> "))


main()