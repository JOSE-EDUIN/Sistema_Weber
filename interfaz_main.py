import tkinter as tk
# from tkinter import ttk
from gui.gui_weber import menu_barra
# from gui.barra_menu import menu_barra
from gui.gui_weber import frame_botones
from gui.pruebaframe import frame_monitoreo
from centrarPantalla import centrar_pantalla
def main():
    gui = tk.Tk()
    
    gui.title("Weber")
    gui.iconbitmap("img/scrapy.ico")
    # gui.geometry('700x500')
    gui.resizable(0,0)
    
    
    app = frame_botones(gui = gui) 
    menu=menu_barra()
    menu.barra_menu(gui, app)
    
    # monitoreo = frame_monitoreo(gui= gui)
    centrar_pantalla(gui, 500, 700)
    
    gui.mainloop()
    
if __name__ == "__main__":
    main()