def encontrar_palavra (nome_arquivo, palavara):
    try:
        with open(nome_arquivo) as arquivo:
            texto= arquivo.readlines()
            cont= 0
            for linha in texto:
                if palavara.lower () in linha.lower():
                    cont+=1
                    print(f'Palavra {palavara.lower()} encontrada! \n' f'Qtd palavras encontradas {cont}')
    except FileNotFoundError :
        print ('Arquivo não encontrado ')


def main ():
    nome_arquivo= 'novo_texto.txt'
    palavara=input('Qual palavara esta procurando -> ')
    encontrar_palavra(nome_arquivo, palavara)


main()