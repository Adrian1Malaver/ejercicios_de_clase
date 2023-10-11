import tkinter as tk
from PIL import Image, ImageTk
from juego import Juego
import time

class Interfaz:
    def __init__(self, master, juego):
        self.master = master
        self.master.title(f"Juego de Cartas ({juego.mazo.__class__.__name__})")
        self.juego = juego

        self.frame_casa = tk.Frame(self.master, width=400, height=400)
        self.frame_casa.pack(side=tk.LEFT)

        self.frame_jugador = tk.Frame(self.master, width=400, height=400)
        self.frame_jugador.pack(side=tk.RIGHT)

        self.mostrar_cartas(self.juego.jugador1.cartas, self.frame_casa)
        self.mostrar_cartas(self.juego.jugador2.cartas, self.frame_jugador)

    def mostrar_cartas(self, cartas, frame):
        self.imagenes = []
        for i, carta in enumerate(cartas):
            img_path = f"C:/Users/Lenovo/Downloads/p1/{self.juego.mazo.__class__.__name__}/{carta.pinta}{carta.valor}.png"
            img = Image.open(img_path)
            img.thumbnail((80, 120))
            img = ImageTk.PhotoImage(img)
            self.imagenes.append(img)
            tk.Label(frame, image=img).grid(row=0, column=i)
            frame.update()
            time.sleep(5)