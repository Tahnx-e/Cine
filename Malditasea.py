import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("No voy a quemarme mas el cerebro ideando un nombre, que alguien mas se lo ponga alv")
root.geometry("1500x700")

Cartelera = tk.Label(
    root, 
    text="Cartelera"
)
Cartelera.pack()

#Como les valio madre las peliculas

p3 = Image.open("persona3.png")
p3 = p3.resize((200,280))
p4 = Image.open("persona4.png")
p4 = p4.resize((200,280))
p5 = Image.open("persona5.png")
p5 = p5.resize((200,280))

p3 = ImageTk.PhotoImage(p3)
p4 = ImageTk.PhotoImage(p4)
p5 = ImageTk.PhotoImage(p5)

def detalles():
print("Aparecen los asientos ocupados, o algo asi, no s[e]")

peli1 = tk.Button (
    root,
    image=p3
)
peli1.pack()

root.mainloop()