acao = 'fudeu'
pessoa = 'Jamelao'

#printar porra jamelao tu me fodeu ein
print ('Porra {1}, tu me {0} ein'.format(acao, pessoa))


#Uns decimais locos
print('{0:.3}'.format(1.0/3))

#underline
print('{0:_^11}'.format('babaovo'))

#printar eu matheus sou a lenda
print('Eu, {name}, sou a {type}'.format(name='Matheus', type="A Lenda"))


#colocar espaço no fim do print, pois o print não dá espaço
print('ai', end=' ')
print('jesus apaga', end=' ')
print('a luz')


#aspas
print('I\'m a lenda')


#quebra de linha
print('Eu sou \nA lenda')
print('este sou eu \
 este é você')

#variaveis     "variaveis nao podem comecar com numero"
name = raw_input("Diga aonde voce vai: ")
print ('{0}, entao eu vou varrendo'.format(name))


#Soma de variavel com constante
i = raw_input("Digite sua idade: ")
i2 = i + 5
print(str(i2)) #esse codigo tá errado

#sominha daora
g = 5
print(g)
g = g + 5
print (g) #comando abaixo pra escrever em mais de 1 linha
s = ''' Ainda assim, existem dúvidas a respeito de como a contínua expansão de nossa atividade causa
 impacto indireto na reavaliação dos procedimentos normalmente adotados.'''

#varios comenados em 1 linha
gg = 6; print(gg); #com ou sem ponto e virgula no final


#Operações de adição, subtração e afins
print('Consulte https://python.swaroopch.com/op_exp.html')


#mudando ordem de operação
(2 + 2) * 6 #resultado será 24

#expressões
batata = 5
arroz = 3
preco = batata * arroz
print 'Preco da batata com arroz tah', 2 * (preco + arroz)





#Condicionais e controle de fluxooo
number = '2'

irmaos = raw_input("Quantos irmaos voce tem? ")
if irmaos == number:
    print('Eh nois')
elif irmaos > number:
    print("podicre")
else:
    print('Seu Jaguara')
print("VAMO Q VAMOOOO") # esse comando irá rodar independente da resposta


#Condicional que só finaliza o processo quando voce acerta (Loop)
number = '2'
running = True 

while running:
    irmaos = raw_input("Quantos irmaos eu tenho? ")

    if irmaos == number:
        print('Eh nois')
        running = False
    elif irmaos > number:
        print("um pouco menos ne campiao")
    else:
        print("nao tao pouco assim seu talarico")
#else:
    #print('Seu Jaguara') 
print("VAMO Q VAMOOOO")


#printar sequencia usando o for
for e in range(1, 5):
    print(e)
else:
    print('numero de vezes q quebrei o osso da clavicula')
print('gg win')


#possivel realizar operacoes 
for e in range(1, 5):
    print(e ** -5) #exponencial
else:
    print('tamanho da minha auto estima ao longo do tempo')
print('ok')

#uso de break, com a resposta certa para
while True:
  
    eu = raw_input('diga meu nome: ')
    if eu == 'Matheus':
    	break   
print ('Q bixo', len(eu))
print ('valeu') 


#se valor menor q 3 caracteres, continua, se for quit, encerra
while True:
  
    eu = raw_input('diga meu nome: ')
    if eu == 'quit':
    	break   
    if eu > 3:
        print('Too Small')
        continue
print ('Q bixo', len(eu))



#mesmo com a resposta correta continua
while True:
  eu = raw_input('diga meu nome: ')
  if eu == 'quit':
  	break   
  if len(eu) < 3:
  	print('Too Small')
  	continue
  print('ja deu moises')

