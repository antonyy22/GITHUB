def converter(texto):
    try:
        num= float(texto)
        print(f'{type(num)} | {num}')
        print(num * 'a')
        return True
    except ValueError:
        print('O valor nao e um numero ')
        print('tente novamente')
        return False
    except TypeError:
        print('voce esta tentando usar um tipo invalido ')
        print('tente novamente')
        return False
    
def obter_informacao():
    while True:
        info= input('informe um numero -> ')
        if converter(info):
            break

def main():
    obter_informacao()


main()