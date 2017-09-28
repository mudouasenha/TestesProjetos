import json


arq = open('bagulho.json', 'r')
jsons = arq.read()
dados = json.loads(jsons) 

lista_de_pontos = []
for point in dados['points']:
    lista_de_pontos.append(point['rfid'] + '-' + point['action'])

final = ';'.join(lista_de_pontos)

print final