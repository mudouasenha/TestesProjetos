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
lista1.sort() #desse modo altera permanentemente a organizacao da lista
print('a lista em ordem alfabetica eh', lista1)


print('primeiro item da lista: ', lista1[0])
maja = lista1[0]
del lista1[0]

print ('comprei ', maja)
print ('agora soh tenho ', lista1)






####USANDO TUPPLE
#Tupple funciona para não alterar permanentemente uma lista
lista2 = ('macaco', 'cachorro', 'passaro')
print('os animais sao', lista2)

novalista2 = 'jiboia', 'jararaca', lista2
print('numero de animais novos: ', len(novalista2))
print('todos os animais: ', novalista2)
print('animais da lista antiga: ', novalista2[2])
print('ultimo animal da lista antiga: ', novalista2[2][2])
print('total de animais: ',len(novalista2)-1+len(novalista2[2]))





###DICIONARIO
baby = {'fralda' : 'pampers', 'shampoo' :'jhonsons'}

###ou

baby = {
    'fralda': 'pampers',
    'shampoo': 'jhonsons',
    'sexo': 'masculino',
    'idade': '3 meses'
}


print ('o bebe usa fralda ', baby['fralda']) #entre chaves pra especificar a key no dicionario
print ('o numero de itens de bebe sao', len(baby)) #parenteses para selecionar o dicionario inteiro

del baby['idade']

print ('\nexistem {} itens no dicionario bebe\n'.format(len(baby)))

''' ver melhor essa parada::
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))
'''


#adicionar item no dicionario
baby['naturalidade'] = 'Brasil'

if sexo in baby:
    print('o sexo do bagulho eh:', baby['sexo'])

#




###SEQUENCIASSS


alfabeto = ['a', 'b', 'c', 'd', 'e', 'f']
meunome = 'Matheus'

print ('itens de 0 a 3 sao', alfabeto[0:3])
print ('ultimos dois itens sao ', alfabeto[-2:])
print ('antepenultimo e penultimo itens da lista sao ', alfabeto[-3:-1])
print ('todos os itens sao ', alfabeto[:])


#com string:
print ('primeiras 4 letras sao ', meunome[:4])
print ('duas ultimas letras sao ', meunome[-2:])
##etc etc

##ou
print ('pegando letras de 3 em 3: ', meunome[::3])
print ('de tras pra frente: ', meunome[::-1])
print ('normal: ', meunome[::1])





##FUNCAO SET 
'''funciona mais como uma lista simples, serve para saber se um item estah ou nao em uma lista, por exemplo, ou se estah em duas ao mesmo tempo'''

casa = set(['junior', 'matheus', 'marluce',])
'junior' in casa
#retorna True
'juniorrr' in casa
#retorna False

ape = casa.copy()
ape.add('luis')
ape.issuperset(casa)
#retornará True
#retornaria false se eu inserisse luis dentro de casa
#funciona como um comparador, vendo se o bloco ape contempla casa


print (casa & ape)
