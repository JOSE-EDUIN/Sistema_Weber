from tkinter import *
import tkinter as tk
from tkinter import ttk
from extraccion_dof import *
from weber_dao import manipulacion_db
from centrarPantalla import centrar_pantalla

    
class configuracion():
    
    def __init__(self):
        '''
        clase de configuracion 
        
        '''
                
        self.ventana = Toplevel()
        self.ventana.title("Sistema Weber: Configuración")
        centrar_pantalla(self.ventana, 500, 900)
        # barra_menu(self.ventana)
          # Establecimiento de la conexión a la base de datos
        self.manipulacion = manipulacion_db()
        # self.wordlist = manipulacion.consulta()

        manipulacion2 = manipulacion_db()
        self.urlist = manipulacion2.consulta2()

        self.combobox1=ttk.Combobox()
    
        #Etiquetas de configuracion url
        label_url = Label(self.ventana, text="Seleccionar url: ")
        label_url.grid(row=0,column=0,padx=20, pady=20, sticky="w",ipady=6)
        self.lista_links()
        
        btn_agregar=Button(self.ventana,text="Nuevo", command=self.cambio_direccion)
        btn_agregar.grid(row=0,column=2,padx=5, pady=6, ipady=4, ipadx=8)
        # self.boton1=tk.Button(self.ventana, text="Elegir", command=lambda:[self.boton1.destroy(),self.recuperar(), self.eliminar3()])
        # self.boton1.grid(column=0, row=2)    
        
        # Botones de configuración
        # self.btn_consultar_palabras = Button(self.ventana,text="Ver palabras en lista", command=lambda:[self.aparecer_lista(),self.aparecer_lista2()])
        # self.btn_consultar_palabras.grid(row=0,column=0,padx=20, pady=20, sticky="w",ipady=6)

        #Etiquetas de configuracion palabra clave
        label_palabra = Label(self.ventana, text="Seleccionar palabra clave: ")
        label_palabra.grid(row=1,column=0,padx=20, pady=20, sticky="w",ipady=6)
        self.lista_palabra()
        # self.btn_cambiar_direccion = Button(self.ventana,text="Cambiar dirección web ", command=self.cambio_direccion)
        # self.btn_cambiar_direccion.grid(row=1,column=0,padx=20, pady=20, sticky="w",ipady=6)
        
        #Etiqueta de configuracion de dominio
        label_dominio=Label(self.ventana, text="Seleccionar dominio web")
        label_dominio.grid(row=2,column=0,padx=20, pady=20, sticky="w",ipady=6)
        self.lista_dominio()

        # self.btn_cambiar_dominio = Button(self.ventana,text="Cambiar dominio web ", command=self.cambiar_dominio_web)
        # self.btn_cambiar_dominio.grid(row=2,column=0,padx=20, pady=20, sticky="w",ipady=6)
        label_dominio=Label(self.ventana, text=" ")
        label_dominio.grid(row=3,column=0,padx=20, pady=20, sticky="w",ipady=6)
        
        label_dominio=Label(self.ventana, text=" ")
        label_dominio.grid(row=4,column=0,padx=20, pady=20, sticky="w",ipady=6)
        
        btn_agregar=Button(self.ventana,text="Guardar cambios", command=self.guardar_cambios)
        btn_agregar.grid(row=5,column=2,padx=5, pady=6, ipady=4, ipadx=8)

        self.ventana.mainloop()


    def guardar_cambios(self):
        print (f"url seleccionado: {self.combobox1.get()}")
        print (f"Palabra clave seleccionada: {self.combobox2.get()}")
        print (f"Dominio seleccionado: {self.combobox3.get()}")
        
        manipulacion = manipulacion_db()
        manipulacion.editar_url_usado(self.combobox1.get())
        manipulacion.editar_palabra_usada(self.combobox2.get())
        manipulacion.editar_dominio_usado(self.combobox3.get())
        self.ventana.destroy()
        
        
    def lista_links(self):
        manipulacion2 = manipulacion_db()
        self.urlist = manipulacion2.consulta2()
        self.opcion=tk.StringVar()
        links=(self.urlist)
        self.combobox1=ttk.Combobox(self.ventana, 
                                  width=50, 
                                  textvariable=self.opcion, 
                                  values=links)
        self.combobox1.current(0)
        self.combobox1.grid(row=0, column=1)

    def lista_dominio(self):
        manipulacion2 = manipulacion_db()
        lista_dominios = manipulacion2.consulta3()
        self.opcion2=tk.StringVar()
        dominios=(lista_dominios)
        self.combobox3=ttk.Combobox(self.ventana, 
                                  width=50, 
                                  textvariable=self.opcion2, 
                                  values=dominios)
        self.combobox3.current(0)
        self.combobox3.grid(row=2, column=1)
        self.boton3=tk.Button(self.ventana, text="Nuevo", command=lambda:[self.cambiar_dominio_web()])
        self.boton3.grid(row=2, column=2,padx=5, pady=6, ipady=4, ipadx=8)  
        
        
    # Evento clic botón cambiar dirección web
    def cambio_direccion(self):
        liga= StringVar()
        manipulacion = manipulacion_db()   
        nva_link=Entry(self.ventana,bg="white",textvariable=liga)
        nva_link.grid(row=0,column=3,padx=1, pady=4, ipadx=20,ipady=3) 
        btn_guardar=Button(self.ventana,text="Guardar",command=lambda:[nva_link.destroy(),btn_guardar.destroy(),manipulacion.insertar_cambio_direccion(liga.get()), self.lista_links()])
        btn_guardar.grid(row=0,column=4,padx=5, pady=6, ipady=4, ipadx=8)


    # Evento clic botón cambiar dominio web
    def cambiar_dominio_web(self):
        dominio= StringVar()
        manipulacion = manipulacion_db()   
        nva_dominio=Entry(self.ventana,bg="white",textvariable=dominio)
        nva_dominio.grid(row=2,column=3,padx=1, pady=4, ipadx=20,ipady=3) 
        btn_guardar=Button(self.ventana,text="Guardar",command=lambda:[nva_dominio.destroy(),btn_guardar.destroy(),manipulacion.insertar_cambio_dominio(dominio.get()), self.lista_dominio()])
        btn_guardar.grid(row=2,column=4,padx=5, pady=6, ipady=4, ipadx=8)
        

    # Evento botón aparecer lista de palabras
    def lista_palabra(self):
        # wordlist = manipulacion2.consulta()
        # manipulacion = manipulacion_db()
        self.wordlist = self.manipulacion.consulta()
        self.opcion1=tk.StringVar()
        palabras=(self.wordlist)
        self.combobox2=ttk.Combobox(self.ventana, 
                                  width=50, 
                                  textvariable=self.opcion1, 
                                  values=palabras)
        self.combobox2.current(0)
        self.combobox2.grid(row=1, column=1 )
        self.boton2=tk.Button(self.ventana, text="Nuevo", command=lambda:[self.agregar_palabra()])
        self.boton2.grid(row=1, column=2,padx=5, pady=6, ipady=4, ipadx=8) 

    def aparecer_lista2(self):
        opcion=tk.StringVar()
        links = self.urlist
        combo = ttk.Combobox(self.ventana, 
                                    width=10, 
                                    textvariable=opcion, 
                                    values=links)
        combo.grid(row=1,column=3,padx=1, pady=6)

        combo.current(0)

        selec = combo.bind("<<ComboboxSelected>>" ,opcion.get())
        print(selec)
        btn_agregar=Button(self.ventana,text="Usar", command=self.recuperar)
        btn_agregar.grid(row=1,column=4,padx=1, pady=6, ipady=4, ipadx=8)
    

    def recuperar(self):
        sele = self.opcion.get()
        print(sele)


    def agregar_palabra(self):
        palabra= StringVar()
        manipulacion = manipulacion_db()
        nva_palabra = Entry(self.ventana, bg="white", textvariable=palabra)
        nva_palabra.grid(row=1,column=3,padx=1, pady=6, ipady=4, ipadx=8)
        btn_confirmar=Button(self.ventana,text="Guardar", command=lambda:[nva_palabra.destroy(), btn_confirmar.destroy(), manipulacion.insertar_palabra_nueva(palabra.get()), self.lista_palabra()])
        btn_confirmar.grid(row=1,column=4,padx=1, pady=6, ipady=4, ipadx=8)


  