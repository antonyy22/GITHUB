def defeituoso(*num):
    soma= 0
    for n in num:
        soma+=n

    return soma / len(num)
def main ():
    media= defeituoso(4,2,56,7,42,5,3,5,7,8)
    print(f'A media é {media}')

main ()