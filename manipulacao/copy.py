from shutil import copy

def copiar_arquivos():
    copy('test.txt', 'bkp_teste.txt')


def main ():
    copiar_arquivos()

main