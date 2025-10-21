alunos= {}
opcao=-1
while (opcao !=0):
    opcao= int (input('O que deseja fazer?  \n'
                      'Opção 1: Cadastrar Aluno(a) \n'
                      'Opção 2: Exibir média \n'
                      'Opção 3: Exibir aluno(a) com maior nota \n'
                      'Opção 0: Sair \n\n'
                      'Opção -> '))
    if opcao ==1:
        key_aluno= len(alunos) +1
        values_alunos= {}
        nome_aluno= input("Informe o nome do aluno(a) -> ")
        idade_aluno= int (input("Informe a idade do aluno(a) -> "))
        nota_aluno= float (input("Informe a nota do aluno(a) -> "))                      
        values_alunos.update({'nome': nome_aluno,
                              'idade': idade_aluno,
                              'nota': nota_aluno})
        alunos.update ({key_aluno: values_alunos})
        print ()
    elif opcao==2:
        soma_notas= 0
        
        for aluno in alunos.values():
            soma_notas+= aluno ['nota']
        print (f'A média das notas é {soma_notas/ len (alunos)} \n')
    elif opcao ==3:
        maior=0
        id = 0
        for id, aluno in alunos.items():
            if aluno ['nota']> maior:
                maior= aluno ['nota']
                id_aluno= id
        print (f'O aluno com maior nota é {alunos[id_aluno] ['nome']} | Nota {maior}')
    else:
        print ('\n Opção inválda\n')