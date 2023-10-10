# interfaz_frances.py
import tkinter as tk
from PIL import Image, ImageTk
from juego import Juego
import time
class Interfaz:
    def __init__(self, master, juego):
        self.master = master
        self.master.title("Juego de Cartas")
        self.juego = juego

        # Divide la ventana en dos partes
        self.frame_casa = tk.Frame(self.master, width=400, height=400)
        self.frame_casa.pack(side=tk.LEFT)

        self.frame_jugador = tk.Frame(self.master, width=400, height=400)
        self.frame_jugador.pack(side=tk.RIGHT)

        # Muestra las cartas de la casa en la parte izquierda
        self.mostrar_cartas(self.juego.jugador1.cartas, self.frame_casa)

        # Muestra las cartas del jugador en la parte derecha
        self.mostrar_cartas(self.juego.jugador2.cartas, self.frame_jugador)

    def mostrar_cartas(self, cartas, frame):
        self.imagenes = []  # Lista para mantener las referencias a las imágenes
        for i, carta in enumerate(cartas):
            img_path = f"C:/Users/Lenovo/Downloads/p1/MazoFrances/{carta.pinta}{carta.valor}.png"
            img = Image.open(img_path)
            img.thumbnail((80, 120))
            img = ImageTk.PhotoImage(img)
            self.imagenes.append(img)  # Agrega la referencia a la lista
            tk.Label(frame, image=img).grid(row=0, column=i)
            frame.update()  # Necesario para actualizar el frame
            time.sleep(5)