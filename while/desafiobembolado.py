usuario= 'gremio'
senha = '1903'
tentativas = 3

while tentativas > 0:
    if input ("Informe o usuario -> ") == usuario:
        if input ("Informe a senha -> ") ==senha :
            print ("Bem vindo", usuario)
            break
        else: 
            print ("Senha incorreta, tente novamente")
            tentativas -=1
            print ("Tentativas restante", tentativas)
    else:
        print("Usuario incorreto tente novamente")
    tentativas -=1
    print ("Tentativas restante", tentativas)
