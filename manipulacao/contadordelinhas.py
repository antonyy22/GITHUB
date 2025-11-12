def contar_linhas ():
    try:
        with open  ('log.txt') as arquivos:
            return len(arquivos.readlines())
        
    except FileNotFoundError:
        print('ARQUIVO NÂO ENCONTRADO ')

def main ():
    qtd_linhas = contar_linhas()
    print (f'O arquivo lido tem {qtd_linhas} linhas! ')

main()