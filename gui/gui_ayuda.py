from tkinter import *
import tkinter as tk
from tkinter import ttk
from centrarPantalla import centrar_pantalla
from gui.buttonAyuda import Linkbutton
import webbrowser

class ayuda_weber():
    
    def __init__(self):
        # self.ventana_padre=gui
        self.ventana = Toplevel()
        self.ventana.title("Ayuda")
        self.ventana.iconbitmap("img/weberIcon.ico")
        centrar_pantalla(self.ventana, 150, 250 )
        ## Provoca que la ventana tome el focus
        self.ventana.focus_set()
          ## Deshabilita todas las otras ventanas hasta que
        ## esta ventana sea destruida.
        self.ventana.grab_set()
    
        ## Indica que la ventana es de tipo transient, lo que significa
        ## que la ventana aparece al frente del padre.
        # self.ventana.transient(master=self.ventana_padre)
        self.create_widgets()
        
    def create_widgets(self):
        
        self.titulo = Label(self.ventana, text="            Sistema de Consultas DOF       ")
        self.titulo.config(font=("Helvetica", 10, "bold"))
        self.titulo.grid(row=0, column=0)
        self.titulo = Label(self.ventana, text="      Si necesita conocer mas acerca del \n      funcionamiento del sistema puede \n      consultar la siguiente:")
        self.titulo.grid(row=1, column=0)
        self.link = Linkbutton(self.ventana,
            text="Documentacion del sistema", command=self.link_clicked)
        self.link.grid(row=2, column=0)
    
    def link_clicked(self):
        webbrowser.open("https://nasa.com.mx/")
        
        