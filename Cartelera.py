#Con lo mucho que me gusta tener un desmadre en mi codigo TwT

from PIL import Image, ImageTk
import tkinter as tk

class Cartelera:
    def __init__(self, root, peliculas):
        self.root = root
        self.peliculas = peliculas
        self.imagenes = []
        self.frame = tk.Frame(self.root)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        cartelera = tk.Label(
        self.frame, 
        text="Cartelera",
        font="Arial, 24"
)
        cartelera.grid(row=0, column=0, columnspan=3)


        self.boton()

#los ciclos de python me confunden bastante
    def boton(self):
        for i, pelicula in enumerate(self.peliculas):
            imagen = Image.open(pelicula.imagen)
            imagen = imagen.resize((200,280))

            imagen = ImageTk.PhotoImage(imagen)

            self.imagenes.append(imagen)

            boton = tk.Button(
                    self.frame,
                    image=imagen
            )

            name = tk.Label (
                self.frame,
                text = pelicula.nombre,
                font= "Arial, 24"
            )

            boton.grid(row=1, column=i, padx=20, pady=20)
            name.grid(row=2, column=i, padx=20, pady=20)



 