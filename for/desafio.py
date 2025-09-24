ps = input ("Informe a palavra secreta -> ")
pe= ['-'] * len(ps)
cl= ''
ten= 5

for t in range (ten+1):
    cl = input ("Chute uma letra", pe )
    for tt in range (len(ps)):
        if pe [tt]== cl:
            pe[t]=cl

    if '-' not in pe:
        print ('Voce venceu!')
    
    print(f"O numero de tentativas restante é {ten- ten}")
else:
    print("Voce perdeu a palavara secreta era", ps)
