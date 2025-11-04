def saudacao (nome, idade):
     return f'Olá {nome}, Parabens pelo seus {idade} anos '

def main ():
    nome= input ('Informe seu nome -> ')
    idade = input ('Informe sua idade -> ')

    boas_vindas= saudacao(nome, idade)
    print (boas_vindas)

main()