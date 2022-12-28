import tkinter as tk
from gui.gui_weber import menu_barra
from gui.gui_weber import frame_botones
from centrarPantalla import centrar_pantalla

def main():
    gui = tk.Tk()
    gui.title("Sistema de Consultas DOF")
    gui.iconbitmap("img/weberIcon.ico")
    gui.resizable(0,0)
    app = frame_botones(gui = gui) 
    menu=menu_barra()
    menu.barra_menu(gui, app)
    
    centrar_pantalla(gui, 400, 818)
    
    gui.mainloop()
    
if __name__ == "__main__":
    main()