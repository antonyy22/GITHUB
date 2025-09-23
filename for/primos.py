qtd= 0
for num in range (1,1000):
    nud= 0
    for num2 in range (1,num+1):
        if num % num2 ==0:
            nud+=1
    if nud ==2:
        print ("numero primo", num)
        qtd +=  1
    if qtd ==20:
        break