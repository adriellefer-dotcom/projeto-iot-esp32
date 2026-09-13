# Nome: Adrielle da Silva Ferreira
# Grupo: 113

def conecta(ssdi, senha):
    import network
    import time
    
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssdi, senha)
    
    for t in range(50):
        if station.isconnected():
            break
        time.sleep(0.1)
    
    return station