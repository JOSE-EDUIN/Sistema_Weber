from tkinter import *
import tkinter as tk

from PIL import Image, ImageTk
from itertools import count

class ImagenLabel(tk.Label):
    """creamos una label para meter el gif"""
    def cargar_gif(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.tiempo = im.info['duracion']
        except:
            self.tiempo = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def bajar_gif(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.tiempo, self.next_frame)
            
class aparecer_gif():
    '''
    Clase para mostrar gifs
    '''
    def gif_cargando():
        # self.row = row
        # self.column = column
        lbl1 = Label(text="Conexion a la pagina web")
        lbl1.grid(row=1,column=1,padx=1, pady=4, ipadx=20,ipady=3)
        label = ImagenLabel()
        label.grid(row=1,column=2,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("loading.gif") # nombre o ruta de la imagen