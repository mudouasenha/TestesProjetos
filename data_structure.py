#estruturas de dados

#list
#pode armazenar uma sequencia de itens, pode adicionar, remover e etc da lista (mutable data type)


####
lista1 = ['macarrao', 'salsicha']


print 'Tenho ', len(lista1), 'itens para comprar'

print ('estes itens sao', end=' ') 
for item in lista1:
  print (item, end=' ')
  
  
  
  #método append
#adiciona um item ao fim da lista

lista1.append('feijao') #apenda (minha lista) ao fim da lista
   


#ordenar por ordem alfabetica
lista1.sort()
print('a lista em ordem alfabetica eh', lista1)

