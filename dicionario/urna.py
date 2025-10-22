
candidatos= ('Ralph Inacio 13', 'Joao Cruz 22', 'Roberto Carlos 7', 'Dilma Trump 24')
cann= {}
votusnulos= {}
opcao=-1
while (opcao !=0):
    opcao= int (input('O que deseja fazer?  \n'
                      'Opção 1: Votar em um presidente \n'
                      'Opção 2: Votar nulo \n'
                      'Opção 3: Cadastrar um presidente \n' 
                      'Opção 4: Mostrar ganhador \n'
                      'Opção 0: Sair \n\n'
                      'Opção -> '))
    if opcao ==3:
        can= len(cann) +1
        Candidatoscadastrados= {}
        nome_presidente= input("Informe o nome do Presidente e o numero do presidente -> ")               
        Candidatoscadastrados.update({'nome': nome_presidente,})
        cann.update ({can: Candidatoscadastrados})
        print ()
    elif opcao==1:
        print ('Os presidentes são', candidatos, cann)
        votacao= input("Me diga o numero do candidato ")
        print ('Voto confirmado')
        votos_= {}
        votos_.update({votacao})
    elif opcao==2:
        votus= len(votusnulos) +1
        votosnulos={}
        nulos= input("Para votar nulo digite o numero 0 ")
        votosnulos.update({nulos})
        votusnulos.update({votus :votosnulos})
    elif opcao== 4:
        ganhador= 0
        vencedor= 0
        
        for vencedor, ganhador in votos_.items():


        