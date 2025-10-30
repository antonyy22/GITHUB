def defeituoso(texto):
    cont=0
    vogais=('a', 'e', 'i', 'o', 'u')

    for letra in texto:
        if letra in vogais:
            cont+=1

    return defeituoso

def main():
    qtd=defeituoso(input('Digite o texto -> '))
    print (f'O texto digitado tem {qtd} vogais! ')

main()