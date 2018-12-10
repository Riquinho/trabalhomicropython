import time
import machine

#Faz a leitura dos sensores
#testa variacao de temperatura
def testTemp():
    temp1 =10
    temp2 = 20
    if (temp2 - temp1) >= 8:
	    alarme()



def alarme():
    y12 = machine.Pin('Y12')
    y12(0 if y12() else 1)

def main():
	while True:
	    testTemp()
	    time.sleep(30)
	
main()