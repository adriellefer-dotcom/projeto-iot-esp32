# Grupo: 113
# Alunos: Adrielle da Silva Ferreira
#         João Gabriel Gudiluna Esteves
#         Lindynei Souza dos Santos

from wifi_lib import conecta

import dht
import machine
import time
import urequests

ssid = 'SEU_WIFI'
senha = 'SUA_SENHA'

d = dht.DHT11(machine.Pin(4))
r = machine.Pin(2, machine.Pin.OUT)

API_KEY = 'SUA_API_KEY_THINGSPEAK'

print("Conectando...")
station = conecta(ssid, senha)

if not station.isconnected():
    print("Não conectado!...")
else:
    print("Conectado...")
    
while True:
    d.measure()
    temp = d.temperature()
    umid = d.humidity()
        
    print("Temperatura: {}°C, Umidade:{}%".format(temp,umid))
        
    if temp > 31 or umid > 70:
        r.value(1)
    else:
        r.value(0)
            
    url = "http://api.thingspeak.com/update?api_key={}&field1={}&field2={}".format(API_KEY, temp, umid)
        
    response = urequests.get(url)
    response.close()
        
    print("Dados enviados ao ThingSpeak")
            
    time.sleep(15)
