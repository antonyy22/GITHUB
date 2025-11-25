def obtem_valor():
    try:
        valor= int(input('Informe um valor inteiro -> '))
    except ValueError:
        print('Valor invalido!', end= ' ')
        print('Necessario ser um numero inteiro ')
    else:
        print(f'valor informado e {valor}')
    finally:
        print('programa encerrado ')

def main():
    obtem_valor()


main()