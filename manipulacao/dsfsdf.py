try:
    with open ('meu_nome.txt', 'r') as arquivo:
        print (arquivo.read())
except FileNotFoundError:
    print('arquivo nao encontrado')