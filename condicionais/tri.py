l1= float(input("Me diga o primmeiro lado do triangulo -> "))
l2= float(input("Me diga o segundo lado do triangulo -> "))
l3= float(input("Me diga o primmeiro lado do triangulo -> "))
if l1 + l2 > l3 or l2 + l3 > l1 or l1 + l3 > l2:
    print("E maior")
if l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2 or l2 == l3 and l2 != l1:
    print("É um isosceles")
elif l1!= l2!= l3:
    print ("E um escalaneo")
else:
    ("resto")