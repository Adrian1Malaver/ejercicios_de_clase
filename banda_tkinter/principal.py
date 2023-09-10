
from banda import Banda
from mostrarInstrumento import MostrarInstrumento

b = Banda()
b.crear_banda()
b.afinar_banda()

for musico in b.musicos:
    MostrarInstrumento(musico.instrumento.nombre)
