def converter(texto):
    try:
        num= float(texto)
        print(f'{type(num)} | {num}')
        return True
    except ValueError:
        print('Informacao digitada nao e um numero ')
        print ('Tente novamente')
        return False
    
def obter_informacao():
    while True:
        info= input('Informe um numero -> ')
        if converter(info):
            break


def main():
    
    obter_informacao()

main()