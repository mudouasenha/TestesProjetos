#FUNÇÕES
def e_nois():  # Define o nome de uma funcao
    posicao1 = '1'
    posicao=raw_input('Voce eh fascista ou antifascista? Primeira opcao: 1, segunda opcao, 2: ')
    if posicao == posicao1:
    	print('Eh nois')
    elif posicao > posicao1:
    	print("que horror")
    else:
      print('que horror')
#fim

e_nois()  #roda a funcao



#OUUUUUU

def ehnois():
    print('Chaaaave')
#fim

def oixuxu():
  print('Oixixi')
#fim

oixuxu() #roda a funcao oixuxu
ehnois() #roda a funcao ehnois




#aindanaosei
def funcao_max(a, b):  #define funcao
    if a > b: #se a for maior que b, vai printar que o valor de a eh o maximo
        print a, 'eh o maximo'
    elif a == b: #se a for igual a b, vai printar exatamente isso
        print a, 'eh igual a', b
    else: #qualquer outro valor, vai pr
        print b, 'eh o maximo'

funcao_max(3, 4) #substituiu o valor de a e b por 3 e 4

x = 5
y = 5

funcao_max(x, y) """ roda a funcao com os valores das variaveis x e y, vai rodar um resultado para o A e 
printar, e rodar outro resultado para o B e printar"""



#mesmo programa acima, porém com outros valores e outros if
def funcao_max(a, b):
    if a >= b:
        print a, 'eh o maximo'
    elif a < b:
        print a, 'eh menor que', b
    else:
        print b, 'eh o maximo'

funcao_max(3, 4)

x = 5
y = 5

funcao_max(x, y)



#VARIAVEIS LOCAIS
"""Nesse caso o valor de oibb vai mudar para 25 somente dentro da funcao, apos eu 
definir um novo valor para oibb, mas fora da funcao vai continuar 10"""
oibb = 10

def func(oibb):
    print 'valor de oibb ainda eh', oibb
    oibb = 25
    print 'valor de oibb mudou para', oibb
#

func(oibb)

print 'Agora o valor voltou pra', oibb



#VARIAVEIS GLOBAIS
"""O valor foi mudado permanentemente mesmo mudando o valor da variavel somente na funcao, porem
com o comando global"""
haha = 10

def func():
    global haha
    print 'valor de haha ainda eh', haha
    haha = 25
    print 'valor de haha mudou para', haha
#

func()

print 'Agora o valor se manteve', haha




#rodar comando varias vezes
def say(message, times = 1):
    print(message * times) #message e times sao parametros
#
say('oioi')
say('Amigo ', 5) #dirah  amigo 5 vezes




#funcao com varios valores
def function(a=10, b=25, c=30):
    print'A tem o valor ', a, ', B tem o valor', b, ', e C tem o valor ', c
#

function(5, 10) #nesse caso o valor de a e b serao redefinidos de acordo com o que foi colocado
function(b=15, a=25) #nesse caso b será substituido por 15, a por 25 e c se manterah
function(9, c=8) #aqui o a terah valor redefinido, c tambem, e b se manterah
#ordem das variaveis pode mudar como voce quiser, exceto assim: (c=15, 4)




def outracoisa(a=5, *numero, **matricula):
    print ('a', a)

    for item_numero in numero:
        print('numero da chamada eh', numero)

    for primeirinha_parte, segundinha_parte in matricula.items():
        print(primeirinha_parte, segundinha_parte)


print(outracoisa(10,1,2,3,Matheus=1410007006,Thiago=1410005005,Vinicius=1410006545))




#varias coisas loucas
def outracoisa (a=5, *numero, **matricula): #criando dois parametros
    print 'a', a

    for numero_chamada in numero: #para variavel nos parametros de numero, printar numero de chamada
        print 'numero da chamada eh', numero_chamada

    #parametro espera dois valores, isto que define o fim da primeira variavel com o da segunda    
    for primeirinha_parte, segundinha_parte in matricula.items(): 
        print primeirinha_parte, segundinha_parte


print outracoisa(10, 1,2,3, Matheus=1410,Thiago=1411,Vinicius=1412) # pega o primeiro valor de a, depois seguem os valores de parametro ate mudar a variavel




#uso da funcao return
def funcao1(x, y): #dependendo do valor de x indicado ao rodar a funcao, vai retornar um ou outro numero
    if x > y:
        return x
    elif x == y:
        return y
    else:
        return y
#

print funcao1(5, 6)
    
#####OBSERVACOES SOBRE O RETURN 
#return none = retornar nada
#somente return = retornar nada
#None = significa Nothingness, ou seja, nada


#codigo a corrigir, objetivo eh mostrar os valores a partir do valor digitado em x
def funcao1():
    global x
    x=raw_input("coloque um numero: ")
    global y
    y=6
    if x >= y:
        return y
    elif x < y:
        return 'quase'
    else:
        return 'errrrouuu'
#

print funcao1()


#significa um bloco vazio de proposicoes
def some_function():
    pass

##





#DOCUMENTOSSSS, PARTE IMPORTANTE E SIMPLES
#O que o .__doc__ faz: roda o comando a partir da funcao com os valores das variaveis ja definidos
def funcao2(x, y):
    x=int(x) #transforma em valor inteiro se possivel
    y=int(y)
    if x > y:
        print 'errado?'
    else:
        print'Acerto mizeravi'

funcao2(7, 6)
print funcao2.__doc__






