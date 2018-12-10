import time
import dht
import machine

#Faz a leitura dos sensores
def leituraDHT():
	leitura = dht.DHT11(machine.Pin(4))
	leitura.measure()
	#leitura.humidity()
	temp1 = leitura.temperature() 
	time.sleep(60)
	leitura = dht.DHT11(machine.Pin(4))
	leitura.measure()
	#leitura.humidity()
	temp2 = leitura.temperature()

	if (temp2 - temp1) == 8:
	    alarme()
        

def alarme():
    y12 = machine.Pin('Y12')
    y12(0 if y12() else 1)


def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('essid', 'password')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
	
def main():
	while True:
	    leituraDHT()
	    time.sleep(30)
	
main()
