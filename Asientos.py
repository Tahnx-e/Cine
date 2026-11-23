#Ya me dio sueño

import tkinter as tk
from tkinter import messagebox

asientos_ocupados = {}

class Asientos: 
    def __init__(self, pelicula, horario):
        self.pelicula = pelicula
        self.horario = horario
        self.clave = (pelicula.nombre, horario.hora)

        self.ocupados = asientos_ocupados.setdefault(
            self.clave, set()
        )

        self.seleccionados = set()
        self.ventana = tk.Toplevel()
        self.ventana.title("Seleccionar asientos")
        self.ventana.geometry("650x600")
        self.mostrar()

    def mostrar(self):
        titulo = tk.Label(
            self.ventana,
            text=self.pelicula.nombre,
            font=("Arial, 15")
        )
        titulo.pack(pady=10)

        info = tk.Label(
            self.ventana,
            text=f"Funcion: {self.horario.hora}",
            font=("Arial", 12)
        )
        info.pack()

        pantalla = tk.Label(
            self.ventana,
            text = "Que diavlos",
            font=("Arial", 14),
            bg="gray",
            fg="white",
            width=35
        )
        pantalla.pack(pady=20)

        self.frame_asientos = tk.Frame(self.ventana)
        self.frame_asientos.pack()
        self.botones = {}
        filas = ["A", "B", "C"]
        columnas = range (1, 5)

        for i, fila in enumerate(filas):
            for columna in columnas:
                asiento = f"{fila}{columna}"

                boton = tk.Button(
                    self.frame_asientos,
                    text = asiento,
                    width=4,
                    height= 2,
                    command=lambda a=asiento:
    self.seleccionar(a)
                )

                boton.grid (row=i, column=columna, padx=4, pady=4)

                self.botones[asiento] = boton

                if asiento in self.ocupados: 
                    boton.config(
                        bg="red",
                        state="disabled"
                    )
                else: 
                    boton.config(bg="green")

        elcosodearriba = tk.Label(
                    self.ventana,
                    text="Verde: Disponible  |  Rojo: Ocupado  |  Azul: Seleccionado"
                )
        elcosodearriba.pack(pady=15)

        self.resumen = tk.Label(
                    self.ventana,
                    text= "Asientos seleccionados: 0 | Total: $0",
                    font = ("Arial", 12)
                )
        self.resumen.pack(pady=10)

        self.confirmar = tk.Button(
                    self.ventana, 
                    text="Continuar",
                    font=("Arial", 12),
                    state ="disabled",
                    command=self.continuar
                )

        self.confirmar.pack(pady=10)

    def seleccionar(self, asiento):
            if asiento in self.seleccionados:
                self.seleccionados.remove(asiento)
                self.botones[asiento].config(bg="green")
            
            else:
                self.seleccionados.add(asiento)
                self.botones[asiento].config(bg="blue")
                cantidad = len(self.seleccionados)
                total = cantidad * self.horario.precio

                self.resumen.config(
                    text=f"Asientos seleccionados: {cantidad} | Total: $ {total}"
                )

                if cantidad > 0:
                    self.confirmar.config(state="normal")
                else: 
                    self.confirmar.config(state="disabled")

    def continuar(self):
            cantidad = len(self.seleccionados)
            total = cantidad * self.horario.precio

            asientos = ",".join(sorted(self.seleccionados))

            respuesta = messagebox.askyesno(
            "Confirmar seleccion", 
            f"Pelicula: {self.pelicula.nombre}\n"
            f"Horario: {self.horario.hora}\n"
            f"Asientos: {asientos}\n"
            f"Total: ${total}\n"
            "Desea continuar?"
        )
#Mi teclado no tiene el signo para abrir interrogacionxd

            if respuesta:
                self.ocupados.update(self.seleccionados)
                messagebox.showinfo(
                    "Asientos reservados correctamente"
                )

                self.ventana.destroy()