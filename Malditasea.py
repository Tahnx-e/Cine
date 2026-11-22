import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primer proyecto")
ventana.geometry("400x300")

etiqueta = tk.Label(
    ventana,
    text="¡Hola mundo desde Tkinter!"
)
etiqueta.pack(pady=30)

ventana.mainloop()