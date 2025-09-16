p= (input("Me diga uma palavra "))
v= 0
for l in p:
    if l == 'a' or l == 'e' or l == 'i' or l== 'o' or l =='u':
        v+=1
print("A palavra", p, "tem", v, "vogais")