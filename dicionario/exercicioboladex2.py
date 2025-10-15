estoque= {
    'feijao': '4',
    'arroz': '2',
    'trufas do joao' : '131'
}

estoque['feijao']= 33

print (estoque['feijao'])
print (estoque['arroz'])
print (estoque['trufas do joao'])


del estoque['feijao']
 
estoque.clear()
