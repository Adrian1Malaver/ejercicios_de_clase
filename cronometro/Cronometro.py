from Hora import *
from Minuto import *
from Segundo import *

class Cronometro:
	def __init__(self):
		self.h = Hora()
		self.m = Minuto()
		self.s = Segundo()
		self.parado = False

	def cambiarEstado(self):
		self.parado = not self.parado

	def avanzar(self):
		self.s.avanzar()
		if(self.s.getValor()==0):
			self.m.avanzar()
			if(self.m.getValor()==0):
				self.h.avanzar()

	def getTiempo(self):
		return "{:02d}:{:02d}:{:02d}".format(self.h.getValor(), self.m.getValor(), self.s.getValor())