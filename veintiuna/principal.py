# principal.py
from interfaz import *
from juego import *
import tkinter as tk
from mazo import MazoEspanol, MazoFrances

if __name__ == "__main__":
    root = tk.Tk()

    mazo = MazoFrances()

    juego = Juego(mazo)
    juego.iniciar_juego()
    juego.jugar()
    juego.valorar_juego()

    app = Interfaz(root, juego)
    root.mainloop()