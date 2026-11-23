import tkinter as tk
from PIL import Image, ImageTk
from Cartelera import Cartelera
from Peliculas import Pelicula

root = tk.Tk()
root.title("No voy a quemarme mas el cerebro ideando un nombre, que alguien mas se lo ponga alv")
root.geometry("1500x700")



#Como les valio madre las peliculas
p1 = Pelicula("Persona 3", "imagenes/persona3.png")
p2 = Pelicula("Persona 4", "imagenes/persona4.png")
p3 = Pelicula("Persona 5", "imagenes/persona5.png")

peliculas = [p1, p2, p3]

app = Cartelera(root, peliculas)



root.mainloop()