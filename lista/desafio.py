num1=int  (input("Me diga seu primeiro numero "))
num2= int(input("Me diga seu segundo numero "))
num3= int (input("Me diga seu terceiro numero "))
num4= int(input("Me diga seu quarto numero "))
num5= int (input("Me diga seu ultimo numero "))

lista = [num1, num2,num3,num4,num5]
maior= max(lista)
menor= min (lista)
media= (num1+num2+num3+num4+num5/5)
print("O maior numero é", maior, "o menor numero digitado é", menor, "e a media desses numeros é", media)