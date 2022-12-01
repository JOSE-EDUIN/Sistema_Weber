import tkinter as tk 
# from extraccion_dof import extraccion
from gui.prueba_monitor import ImagenLabel
from gui.monitoreo_gifs import *

class frame_monitoreo (tk.LabelFrame):
    '''
    Clase para definir un frame que servira para contener todo lo que se mostrara en pantalla 
    '''
    # tk.LabelFrame
    def __init__(self, gui = None):
        tk.LabelFrame.__init__(self, gui, text="Monitoreo")
        self.gui = gui 
        # self.pack(expand = True, fill='both')
        # self.config(bg="blue")
        self.config(bd=5)
        self.config(cursor="pirate")
        self.grid(row=0, column=1, padx=5, pady=5)
        self.configure(font=("Arial Rounded MT Bold", 16, "roman"))
        # self.botones2()
        # self.gif_cargando()
        # self.gif_cargando2()
        # self.gif_cargando3()
        # self.gif_cargando4()
        # self.gif_cargando5()
        # self.gif_cargando6()
        # self.gif_cargando7()
    
    def botones2(self):
        '''
        Función que define los botones para ejecutar los procesos completos del weber 
        '''
        
        self.btn_ejecutar = tk.Button(self, text="Ejecutar Servicio 2")
        # self.btn_ejecutar.place(x=60, y=40, width=100, height=30)
        self.btn_ejecutar.grid(column=0, row=0, padx=5, pady=5)  
        
        
    def gif_error_web(self):
        self.lbl1 = Label(self, text="Conexion a la pagina web")
        self.lbl1.grid(row=0,column=0,padx=20, pady=5)
        
        label2 = ImagenLabel(self)
        label2.grid(row=0,column=1,padx=1, pady=4, ipadx=2,ipady=3)
        label2.cargar_gif("incorrecto.png") # nombre o ruta de la imagen


    def gif_cargando(self):
        # self.row = row
        # self.column = column
        self.lbl1 = Label(self, text="Conexion a la pagina web")
        self.lbl1.grid(row=0,column=0,padx=20, pady=5)
        # self.label = ImagenLabel(self)
        # self.label.grid(row=0,column=1,padx=1, pady=4, ipadx=2,ipady=3)
        # self.label.cargar_gif("loading.gif") # nombre o ruta de la imagen
        
        # cargamos gif loading
        label2 = ImagenLabel(self)
        label2.grid(row=0,column=1,padx=1, pady=4, ipadx=2,ipady=3)
        label2.cargar_gif("loading.gif") # nombre o ruta de la imagen

        #Destruimos el label
        label2.after(1000, label2.destroy())
        
        #creamos imagen finalizado para la anterior funcion
        label_correcto = ImagenLabel(self)
        label_correcto.grid(row=0,column=1,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto2.png") # nombre o ruta de la imagen
    
    
    def gif_error_bd(self):
        self.lbl1 = Label(self, text="Conexión a la base de datos")
        self.lbl1.grid(row = 1, column = 0, padx=20, pady=5)
        
        label = ImagenLabel(self)
        label.grid(row=1,column=1,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("incorrecto.png") # nombre o ruta de la imagen
        
        
    def gif_cargando2(self):
        self.row = 1
        self.column = 0
        self.lbl1 = Label(self, text="Conexión a la base de datos")
        self.lbl1.grid(row = 1, column = 0, padx=20, pady=5)
        
        label = ImagenLabel(self)
        label.grid(row=1,column=1,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("loading.gif") # nombre o ruta de la imagen
        
        label.after(1000, label.destroy())
        
        label_correcto = ImagenLabel(self)
        label_correcto.grid(row=1,column=1,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto2.png") # nombre o ruta de la imagen
        
    
    def gif_error_busqueda_publicacion(self):
        self.lbl1 = Label(self, text="Buscando publicación nueva")
        self.lbl1.grid(row = 2, column = 0, padx=20, pady=5)
        
        label = ImagenLabel(self)
        label.grid(row=2,column=1,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("incorrecto.png") # nombre o ruta de la imagen
        
            
    def gif_cargando3(self):
        self.lbl1 = Label(self, text="Buscando publicación nueva")
        self.lbl1.grid(row = 2, column = 0, padx=20, pady=5)
        
        label = ImagenLabel(self)
        label.grid(row=2,column=1,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("loading.gif") # nombre o ruta de la imagen
        
        label.after(1000, label.destroy())
        
        label_correcto = ImagenLabel(self)
        label_correcto.grid(row=2,column=1,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto2.png") # nombre o ruta de la imagen
        
    
    def gif_error_extraer_link(self):  
        self.lbl1 = Label(self, text="Extrayendo links de publicaciones")
        self.lbl1.grid(row = 3, column = 0, padx=20, pady=5)
        
        label = ImagenLabel(self)
        label.grid(row=3,column=1,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("incorrecto.png") # nombre o ruta de la imagen
        
              
    def gif_cargando4(self):
        self.lbl1 = Label(self, text="Extrayendo links de publicaciones")
        self.lbl1.grid(row = 3, column = 0, padx=20, pady=5)
        
        label = ImagenLabel(self)
        label.grid(row=3,column=1,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("loading.gif") # nombre o ruta de la imagen
        
        label.after(1000, label.destroy())
        
        label_correcto = ImagenLabel(self)
        label_correcto.grid(row=3,column=1,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto2.png") # nombre o ruta de la imagen
        
        
    def gif_error_enviar_link(self):
        self.lbl1 = Label(self, text="Enviando links a la base de datos")
        self.lbl1.grid(row = 0, column = 2, padx=20, pady=5)
        
        label = ImagenLabel(self)
        label.grid(row=0,column=3,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("incorrecto.png") # nombre o ruta de la imagen
        
            
    def gif_cargando5(self):
        self.lbl1 = Label(self, text="Enviando links a la base de datos")
        self.lbl1.grid(row = 0, column = 2, padx=20, pady=5)
        
        label = ImagenLabel(self)
        label.grid(row=0,column=3,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("loading.gif") # nombre o ruta de la imagen
        
        label.after(1000, label.destroy())
        
        label_correcto = ImagenLabel(self)
        label_correcto.grid(row=0,column=3,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto2.png") # nombre o ruta de la imagen


    def gif_error_envio_correo(self):
        self.lbl1 = Label(self, text="Enviando correo electronico")
        self.lbl1.grid(row = 1, column = 2, padx=20, pady=5)
        
        label = ImagenLabel(self)
        label.grid(row=1,column=3,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("incorrecto.png") # nombre o ruta de la imagen
        
        
    def gif_cargando6(self):
        self.lbl1 = Label(self, text="Enviando correo electronico")
        self.lbl1.grid(row = 1, column = 2, padx=20, pady=5)
        
        label = ImagenLabel(self)
        label.grid(row=1,column=3,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("loading.gif") # nombre o ruta de la imagen
        
        label.after(1000, label.destroy())
        
        label_correcto = ImagenLabel(self)
        label_correcto.grid(row=1,column=3,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto2.png") # nombre o ruta de la imagen
        
    def gif_error_fin_proceso(self):
        self.lbl1 = Label(self, text="Proceso finalizado con éxito")
        self.lbl1.grid(row = 2, column = 2, padx=20, pady=5)
        
        label = ImagenLabel(self)
        label.grid(row=2,column=3,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("incorrecto.png") # nombre o ruta de la imagen
        
            
    def gif_cargando7(self):
        '''
        funcion para gif 7
        '''
        self.lbl1 = Label(self, text="Proceso finalizado con éxito")
        self.lbl1.grid(row = 2, column = 2, padx=20, pady=5)
        
        label = ImagenLabel(self)
        label.grid(row=2,column=3,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("loading.gif") # nombre o ruta de la imagen
        
        label.after(1000, label.destroy())
        
        label_correcto = ImagenLabel(self)
        label_correcto.grid(row=2,column=3,padx=1, pady=4, ipadx=2,ipady=3)
        label_correcto.cargar_gif("correcto2.png") # nombre o ruta de la imagen
        
    def gif_cargando8(self):
        '''
        funcion para gif 7
        '''
        self.lbl1 = Label(self, text="Proceso finalizado con éxito")
        self.lbl1.grid(row = 2, column = 2, padx=20, pady=5)
        
        label = ImagenLabel(self)
        label.grid(row=2,column=3,padx=1, pady=4, ipadx=2,ipady=3)
        label.cargar_gif("loading.gif") # nombre o ruta de la imagen
        
        # label.after(1000, label.destroy())            
        # label_correcto = ImagenLabel(self)
        # label_correcto.grid(row=2,column=3,padx=1, pady=4, ipadx=2,ipady=3)
        # label_correcto.cargar_gif("correcto2.png") # nombre o ruta de la imagen
        
    def mostrar_fondo_we(self):
        '''
        funcion para fondo principal
        '''
        self.fondo=Image.open("img/WeberPrincipal.jpeg")
        self.fondo=self.fondo.resize((550,475), Image.ANTIALIAS)
        
        self.img_fondo=ImageTk.PhotoImage(self.fondo)
        self.fondo_principal=Label(self.gui, image=self.img_fondo)
        self.fondo_principal.grid(row=0, column=1)
        
    def aceptar_resultados(self, destruir):
        '''
        Boton de aceptar en el frame de monitoreo y elimina el frame monitoreo
        '''
        btn_aceptar=tk.Button(self.gui, text="Aceptar", command=lambda:[destruir, self.mostrar_fondo_we()])
        btn_aceptar.grid(row=3,column=3,padx=5, pady=4, ipadx=2,ipady=3)