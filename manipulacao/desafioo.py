def gerar_boletim(aluno):
    with open ('boletim.txt', 'w') as boletim:
        for chave, valor in aluno.items():
            if type(valor)!= float:
                boletim.write(f'{chave} | {valor} \n')
            else:
                boletim.write(f'{chave} | {valor:.2f} \n')
    
    for chave, valor in aluno.items():
        if type(valor)!= float:
            print(f'{chave} | {valor}')
        else:
            print(f'{chave} | {valor:.2f}')

def calcular_boletim(aluno):
    media= (aluno ['Nota_1'] + aluno ['Nota_2'] + aluno ['Nota_3'])
    status_aluno= ''
    if media>=7:
        status_aluno = 'aprovado'
    else:
        status_aluno = 'reprovado'

    aluno.uptade({'Media' : media,
                  'status_aluno' : status_aluno})
    gerar_boletim(aluno)


def obtem_info():
    aluno= {'Nome': '',
            'Nota 1': 0,
            'Nota 2': 0,
            'Nota 3': 0}
    aluno ['Nome']= input ('Informe o nome do aluno -> ')
    aluno ['Nota 1']= float (input("Informe a primeira nota -> "))
    aluno ['Nota 2']= float(input('Informe sua segunda nota -> '))
    aluno ['Nota 3']= float (input('Informe sua terceira nota -> '))
    
    return aluno


def main():
    aluno= obtem_info()
    calcular_boletim(aluno)


main()

