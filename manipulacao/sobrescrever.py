def obter_texto():
    texto= input('Digite o novo texto -> ')
    print ('Novo texto obtido!!! ')
    return texto


def escrever ():
    with open ('novo_texto.txt', 'w') as arquivo:
        arquivo.write(obter_texto())
        print('Novo texto gravado ')

def main ():
    escrever()


main ()