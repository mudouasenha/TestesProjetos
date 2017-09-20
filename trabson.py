import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("projetointegrador/julinho/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.payload)
    rota = {}
    rota['funcao1'] = [f]
    rota['funcao2'] = [d]
    rota['funcao3'] = [e]
        def comandos(f, d, e):
            print 
    rota['rota1'] = ['funcao1', 'funcao2', 'funcao3']
    rota['rota2'] = ['IDfuncao2, IDfuncao2, IDfuncao2']
    if msg.payload == 'rota1':
        print rota['rota1']
    elif msg.payload =='rota2':
        print rota['rota2']
    else:
        print 'inexistente'
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("iot.eclipse.org", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
