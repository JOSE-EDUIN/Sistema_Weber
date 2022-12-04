import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.config(width=300, height=200)
root.title("Botón en Tk")
img_boton = tk.PhotoImage(file="agregar.png")
boton = ttk.Button(image=img_boton)
boton.place(x=50, y=50)
root.mainloop()