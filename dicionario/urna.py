opcao= -1
candidatos= []
senha_encerrar= []
encerrar_votacao= 1900
contagem_votos =     []

while opcao!=senha_encerrar:
    opcao= input("O que deseja fazer? \n"  
                  "Opção 1: Cadastrar candidato \n"
                   "Opção 0: Sair \n"
                    "Opção -> "     )
    
    if opcao.isdigit():
        opcao= int (opcao)


        if opcao==1:
            qtd_candidatos= int (input("Quantos candidatos deseja cadastrar? "))
            for c in range (1,qtd_candidatos+1):
                candidato=[]
                nome= input(f'Nome do candidato {c} -> ')
                num_candidato= int (input(f"Numero do candidato {c}-> "))

                candidato.append(nome)
                candidato.append(num_candidato)
                candidatos.append(tuple(candidato))
             

            print ('\n\n')
        
        elif opcao==2:
            voto= -1
            while voto != encerrar_votacao:
                for candidato in candidatos:
                    print (f'Candidato {candidato(0)} | Numero {candidato(1)}')
                voto= int (input("Vote no numero de um candidato ->"))
                for candidato in candidatos:
                    if voto ==candidato[1]:
                        if candidato[0] not in contagem_votos:
                            contagem_votos.updat ({candidato{0}:1})
                            break