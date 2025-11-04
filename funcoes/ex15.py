def verificar_primo (numero):
    divisoes= 0
    for n in range (1, numero +1):
        if numero % n == 0:
            divisoes += 1

    if divisoes == 2:
        return True
    else:
        return False
    

def main ():
    numero= int(input('Me diga o seu numero -> '))
    resultado= verificar_primo(numero)
    print(' O numero é primo?', resultado )

main ()