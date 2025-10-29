def defeituoso(num):
    if num % 2== 0:
        return 'par'
    else:
        return 'impar'
def main ():
    resultado=defeituoso(int(input("Informe um numero ->")))
    print (resultado)

main()