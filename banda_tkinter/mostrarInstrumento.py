import tkinter as tk
from tkinter import *
from random import choice
from instrumento import Guitarra, Maracas, Charrasca

class MostrarInstrumento:
    def __init__(self, nombre_instrumento):
        self.nombre_instrumento = nombre_instrumento
        self.ventana = tk.Tk()
        self.ventana.title("Mostrar Instrumento")
        
        imagen_path = f"{self.nombre_instrumento.lower()}.png"  
        imagen = PhotoImage(file=imagen_path)
        
        self.imagen_label = tk.Label(self.ventana, image=imagen)
        self.imagen_label.imagen = imagen  
        self.imagen_label.pack()

        self.ventana.mainloop()
