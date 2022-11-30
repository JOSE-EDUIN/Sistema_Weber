import tkinter as tk 
from gui.gui_configuraciones import configuracion
from gui.gui_weber import frame_botones


class menu_barra():
    
    def __init__(self):
        pass
    
    def archivo_nuevo_presionado(self, frame_servicio):
        '''
        llama ventana configuraciones
        '''
        frame_servicio.destroy()
        configuracionVentana = configuracion()


    def frame_ejecucion(self):
        '''
        Para ejecucion
        '''
        frame_ejecucion=frame_botones()
        
        
    def barra_menu(self, gui):
        '''
        Funcion para la barra de menú de la aplicación 
        '''
        
        barra_menu = tk.Menu(gui)
        gui.config(menu = barra_menu)
        
        menu_opciones = tk.Menu(barra_menu, tearoff= 0)
        barra_menu.add_cascade(label = "Opciones", menu = menu_opciones)
        menu_opciones.add_command(
            label = "Ejecutar Servicio" ,
            command= self.frame_ejecucion()   
        )
        menu_opciones.add_command(
            label="Configuración del Weber",
            accelerator="Ctrl+A",
            command= lambda:[self.archivo_nuevo_presionado(frame_botones)]
        )
        # Asociar el atajo del teclado del menú "Nuevo".
        gui.bind_all("<Control-a>", self.archivo_nuevo_presionado)
        menu_opciones.add_separator()
        menu_opciones.add_command(label = "Salir", command= gui.destroy )
        
        menu_ayuda = tk.Menu(barra_menu,  tearoff= 0)
        barra_menu.add_cascade(label= "Ayuda", menu= menu_ayuda)
        menu_ayuda.add_command(label= "Ayuda")
        menu_ayuda.add_command(label= "Version")
