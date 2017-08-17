#geralmente dar import em todos os arquivos antes de iniciar o código
#import em todo o codigo
import modulo1

#importação seletiva
#importa somente a funcao jamelao
from doce import jamelao():

# Bibliotecas que não estão no python:
# Math


#uso de math
import math #importa tudo
from math import ceil, sqrt #importa somente ceil e sqrt
#ceil = arredondar pra cima
#florr = arredondar pra baixo
#trunc = sem arredondamento
#pow = potência
#sqrt = square root
#factorial = fatorial né dããã
#etc




#dá o valor de raiz quadrada e um numero dado
import math
run = raw_input("diga um numero")
raiz = int(sqrt(run))
print 'A raiz quadrada de {} eh {}'.format(run, floor(raiz))



#biblioteca random dá um numero aleatorio dado pelo computador entre 0 e 1
import random
run1 = random.random()
print(run)


#ou em numeros inteiros
import random
run1 = random.ranint()
print(run)



#instalar biblioteca ou modulo que nao eh padrao do python
#em Python Educational ou Pycharm
import #nomedabiblio
# clicar botao direito, lampada vermelha, nstall package




#Instalar no Pycharm Python Educational modulos externos
#pycharm - preferencias - clicar em projeto - alguma coisa interpreter








#biblioteca sys

import sys
for i in sys.argv:
    print i
#
#na hora de rodar:
#python nomedoarquivo.py palavra palavra palavra, define valores usando su proprio comando


#Descobrir diretorio do proprio programa
import os; print(os.getcwd())


print 'the system path is', sys.path, '\n' #printar caminho do modulo



#uso de .pyc
import math.pyc
#modo mais rapido de buscar o modulo, mais eficiente
#byte-compiled files



#descobrir se o modulo foi importado ou se roda sozinho

if __name__ == '__main__': #main = roda sozino, name = nome do modulo
    print 'o programa roda sozinho'
else:
    print 'o programa esta sendo importado'

#






# selecionar função específica dentro de um módulo importado
#supondo que essa função estivesse em um arquivo
import blablabla

#essa seria a função
def funcao2(x, y):
    x=int(x) #transforma em valor inteiro se possivel
    y=int(y)
    if x > y:
        print 'errado?'
    else:
        print'Acerto mizeravi'

funcao2(7, 6)
print funcao2.__doc__


#chama somente essa funcao dentro do modulo e mostra versão
blablabla.funcao2()
print('versao', funcao2.__version__)



#função DIR
#retorna funções, classes, variáveis e argumentos do modulo

import math

#para mostrar os atributos do módulo math
dir(math)


#para mostrar os atributos no módulo atual
dir()

#OBS: criando ou deletando atributos ou variaveis, o dir vai mostrar de acoro com a mudança
a = 5
dir() #mostra o a
del a
dir() #não mostra o a





