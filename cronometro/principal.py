import time
from Cronometro import *

c=Cronometro()
cont=0
while(cont<10000):
	time.sleep(1)
	c.avanzar()
	print (c.getTiempo())
	cont=cont+1