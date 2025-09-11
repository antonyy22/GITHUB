cal= float (input("Me diga um numero -> "))
cal1= float (input("Me diga um segundo numero -> "))
sinal=input("Me diga um sinal para a operacao -> ")

if sinal == "+":
    resultado = cal + cal1
    print("A soma é ", resultado)

elif sinal == "-":
    resultado= cal - cal1
    print("o resultado é", resultado)

elif sinal == "*":
    resultado= cal * cal1
    print("A multiplicacao é", resultado)

elif sinal == "/":
    if cal1 == 0:
        print("Uma das condicoes e zero ")   
    else:
        resultado = cal / cal1
        print("A divisao é", resultado)

else:
    print("Operacao invalida")