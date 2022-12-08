# from tkinter import *
import tkinter as tk 
from extraccion_dof import extraccion
from gui.prueba_monitor import ImagenLabel
from gui.monitoreo_gifs import *
from gui.pruebaframe import frame_monitoreo
from Base_datos_scrapper import conexion_bd
from gui.gui_configuraciones import configuracion
from gui.gui_ayuda import ayuda_weber
import time
from PIL import ImageTk, Image

class menu_barra():
    
    def __init__(self):
        self.configuracion_ventana = None
        self.monitoreo = frame_monitoreo()
    
    def configuraciones_presionado(self):
        '''
        llama ventana configuraciones
        '''
        # self.ventana_press = gui
        self.configuracion_ventana = configuracion()
    
    
    def configuraciones_gui(self):
        # self.ventana = gui
        self.configuracion_ventana=configuracion()
        
    
    def ayuda_gui(self):
        # self.ventana_padre=gui
        self.ayuda_ventana = ayuda_weber()
    
    def mostrar_logo(self, gui):
        '''
        Funcion para llamar el logo en ejecutar servicio
        '''
        label_vacio=Label(gui, text="")
        label_vacio.grid(row=0, column=0)
        fondo=Image.open("img/WeberPrincipal.jpeg")
        fondo=fondo.resize((550,475), Image.ANTIALIAS)
        
        img_fondo=ImageTk.PhotoImage(fondo)
        fondo_principal=Label(gui, image=img_fondo)
        fondo_principal.grid(row=0, column=1)
        
    
    def quit_frame(self):
        self.monitoreo.destroy()
        
    def servicio(self, gui):
        '''
        Servicio en vista
        '''
        # eliminar_widget = configuracion()
        print("lo estoy intentando")
        self.configuracion_ventana = configuracion(gui)
        self.configuracion_ventana.eliminar_configuracion()
        # eliminar_widget.eliminar_configuracion
        # self.frame_servicios=frame_servicio
        
    def barra_menu(self, gui, frame_botones):
        '''
        Funcion para la barra de menú de la aplicación 
        '''
        # frame_botoness = frame_botones
        barra_menu = tk.Menu(gui)
        gui.config(menu = barra_menu)
        
        menu_opciones = tk.Menu(barra_menu, tearoff= 0)
        barra_menu.add_cascade(label = "Opciones", menu = menu_opciones)
        # menu_opciones.add_command(
        #     label = "Ejecutar Servicio"#,
        #     # command= lambda:[self.quit_frame()]
        # )
        
        menu_opciones.add_command(
            label="Configuración del Weber",
            accelerator="Ctrl+a",
            command= lambda:[self.configuraciones_gui()]
        )
        # Asociar el atajo del teclado del menú "Nuevo".
        gui.bind("<Control-a>", self.configuraciones_presionado)
        menu_opciones.add_separator()
        menu_opciones.add_command(label = "Salir", command= gui.destroy )
        
        menu_ayuda = tk.Menu(barra_menu,  tearoff= 0)
        barra_menu.add_cascade(label= "Ayuda", menu= menu_ayuda)
        menu_ayuda.add_command(label= "Ayuda", command=self.ayuda_gui)
        # menu_ayuda.add_command(label= "Version")


class frame_botones (tk.Frame):
    
    def __init__(self, gui = None):
        '''
        Clase para definir un frame que servira para contener todo lo que se mostrara en pantalla 
    
        '''
        tk.Frame.__init__(self, gui)
        self.gui = gui 
        # self.pack(expand = 0, fill='y')
        self.config(height=500, width=30)
        self.config(bg="lightblue")
        # self.pack(side="top", anchor="w")
        self.config(bd=25)
        self.config(cursor="pirate")
        self.grid(row=0, column=0)
        # self.config(width="25", height="500")
        
        self.fondo=Image.open("img/WeberPrincipal.jpeg")
        self.fondo=self.fondo.resize((625,380), Image.ANTIALIAS) #cc475
        
        self.img_fondo=ImageTk.PhotoImage(self.fondo)
        self.fondo_principal=Label(self.gui, image=self.img_fondo)
        self.fondo_principal.grid(row=0, column=1)
        # self.panel_procesos()
        self.botones()
        

        self.extraction = extraccion()
    # def panel_procesos(self):
    
    #     self.label=tk.Label(self , text="| Computacion |",  fg="lime green")
    #     self.label.grid(row = 2, column = 3)
    #     # self.label.pack()
        
    def procesos(self):
        '''
        Función para llamar a los procesos en ejecucion
        '''
        self.fondo_principal.destroy()
        app=frame_monitoreo(gui= self.gui)
        # try:
            
        self.extraction = extraccion()
        self.extraction.acceso_web()
                # conn_bd = conexion_bd()
        self.extraction.conn_bd()
        self.extraction.buscar_69b()
        self.extraction.obtener_link()
        self.extraction.validar_pub_nva()
        self.extraction.notificacion_correo()
            
        # except:
        #     self.extraction.monitoreo.gif_error_fin_proceso()
        #     print("Error al finalizar el proceso ")
        # else:
        #     print("proceso terminado")
            # self.extraction.monitoreo.gif_cargando7()
            # self.extraction.monitoreo.aceptar_resultados(app)
        # return True
    
    def Proceso_finalizado(self):
        
        if self.procesos() == True:
            self.extraction.monitoreo.gif_cargando7()
        
        # if self.procesos() == False:
        #    self.extraction.monitoreo.gif_cargando8() 
           
    def botones(self):
        '''
        Función que define los botones para ejecutar los procesos completos del weber 
        '''
        
        self.btn_ejecutar = tk.Button(self, text="Ejecutar Servicio", command= lambda:[self.procesos()])
        self.btn_ejecutar.grid(column=0, row=0, padx=5, pady=150)    
        self.btn_ejecutar.configure(font=("Bahnschrift SemiBold", 10), bg="PeachPuff2") 
        
        
    
        


