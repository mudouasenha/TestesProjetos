import paho.mqtt.client as mqtt
import json

def not_empty(str):
    return str != ''

def sos(msg):
    print(json.dumps({'sos': int(msg)}))
    pass

def enable(msg):
    print(json.dumps({'enable': int(msg)}))
    pass

def check(msg):
    print(json.dumps({'check': int(msg)}))
    pass
def funcao

def on_connect(client, userdata, flags, rc):
    client.subscribe("julinho/#")

def on_message(client, userdata, msg):
    topic = filter(not_empty, msg.topic.split('/'))  #split transforma em lista, separados   # ex, nesse caso julinho/sos ficaria..  ['julinho', 'sos']
        
    if topic[1] == 'sos':
        sos(msg.payload)
    elif topic[1] == 'enable':
        enable(msg.payload)
    elif topic[1] == 'check':
        check(msg.payload)
            

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)
client.loop_forever()
