# from extraccion_dof import extraccion
from tkinter import tix
import tkinter as tk
from tkinter import ttk

ventana = tix.Tk()
ventana.title("Globo Mensaje")
ventana.geometry("200x200")

tip = tix.Balloon(ventana)

aceptar = tk.Button(ventana, text="Aceptar")
aceptar.pack(pady=50)

tip.bind_widget(aceptar, balloonmsg="Pulse el boton de aceptar")

ventana.mainloop()