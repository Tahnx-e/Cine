import tkinter as tk
from PIL import Image, ImageTk
from Cartelera import Cartelera
from Peliculas import Pelicula
from Horarios import Horario

#Estoy muy confundido hay como 6 horarios, que malas practicas de mi parte

root = tk.Tk()
root.title("No voy a quemarme mas el cerebro ideando un nombre, que alguien mas se lo ponga alv")
root.geometry("1500x700")


#Como les valio madre las peliculas
p1 = Pelicula("Persona 3", "imagenes/persona3.png", [Horario("14:00", 100), Horario("12:00", 100)] )
p2 = Pelicula("Persona 4", "imagenes/persona4.png", [Horario("10:00", 130), Horario("16:00", 130)] )
p3 = Pelicula("Persona 5", "imagenes/persona5.png", [Horario("18:00", 80), Horario("20:00", 80)])

peliculas = [p1, p2, p3]

app = Cartelera(root, peliculas)

#Esta bien feo lo bueno que quiero ser backend xd

root.mainloop()