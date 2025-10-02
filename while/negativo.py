nota = 0
somanotas = 0
media = 0
qtdnotas= 0

while nota >= 0:
    nota= int(input ("Informe sua nota -> "))
    somanotas += nota
    qtdnotas+=1
print ("a media das notas e ", somanotas / qtdnotas )
