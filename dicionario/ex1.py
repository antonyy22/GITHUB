carro= { 
    'marca' : 'volkswagen',
    'modelo' : 'fusca',
    'ano' : 'antes de cristo'
}
print (carro['marca'])
print (carro['modelo'])
print (carro['ano'])

#acessando o valor da chave

print (carro['marca'])



# adicionando chaves

carro[ 'cor'] = 'rosinha bebe'
print (carro['cor'])
  
# atualizando ano
carro['ano']= 2000

print(carro['ano'])



#remover a chave modelo

carro.pop('modelo')

#usando get

print(carro.get('modelo'))



# listando todas as chaves

print (carro.keys())
