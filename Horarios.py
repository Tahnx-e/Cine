#Mas clases, que emocion wuuu (estoy harto)

import tkinter as tk
from Asientos import Asientos

class Horario:
    def __init__(self, hora, precio):
        self.hora = hora
        self.precio = precio


class Funciones:
    def __init__(self, pelicula):
        self.pelicula = pelicula
        self.ventana = tk.Toplevel()
        self.ventana.title = ("Seleccionar horario")
        self.ventana.geometry("500x400")

        self.horarios = pelicula.horarios

        self.mostrar()

    def mostrar(self):
        titulo = tk.Label(
            self.ventana,
            text=self.pelicula.nombre,
            font="Arial, 12"
        )
        titulo.pack(pady=20)

        texto = tk.Label (
            self.ventana,
            text = "Horarios disponibles",
            font = "Arial, 14"
        )
        texto.pack(pady=10)

        for horario in self.horarios:
            boton = tk.Button(
            self.ventana,
            text=f"{horario.hora} - ${horario.precio}",
            font="Arial, 12",
            command=lambda h=horario: self.seleccionar(h)
            )

            boton.pack(pady=8)

    def seleccionar(self, horario):
        Asientos(self.pelicula, horario)