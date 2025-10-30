def defeituoso(temp):
    return (temp * 1.8) + 32



def main ():
    tempf= defeituoso(float(input('informe a temperatura em ° ->')))
    print (f'A temperatura em °F é {tempf}')

main ()