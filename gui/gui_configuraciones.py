from tkinter import *
import tkinter as tk
from tkinter import ttk
from idlelib.tooltip import Hovertip
import tkinter.font as tkFont
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
        label_url = Label(self.ventana, text="Seleccionar URL: ")
        label_url.grid(row=0,column=0,padx=20, pady=20, sticky="w",ipady=6)
        fuente=tkFont.Font(family="Arial Rounded MT Bold", size=11, slant="roman")
        label_url.configure(font=fuente)
        self.lista_links()
        
        img_boton = tk.PhotoImage(file="agregar.png")
        btn_agregar=ttk.Button(self.ventana,image=img_boton, command=self.cambio_direccion)
        btn_agregar.grid(row=0,column=2,padx=5, pady=6, ipady=2, ipadx=2)
        tip=Hovertip(btn_agregar,'Si desea agregar una nueva dirección web, presione este botón')
        # self.boton1=tk.Button(self.ventana, text="Elegir", command=lambda:[self.boton1.destroy(),self.recuperar(), self.eliminar3()])
        # self.boton1.grid(column=0, row=2)    
        
        # Botones de configuración
        # self.btn_consultar_palabras = Button(self.ventana,text="Ver palabras en lista", command=lambda:[self.aparecer_lista(),self.aparecer_lista2()])
        # self.btn_consultar_palabras.grid(row=0,column=0,padx=20, pady=20, sticky="w",ipady=6)

        #Etiquetas de configuracion palabra clave
        label_palabra = Label(self.ventana, text="Seleccionar palabra clave: ")
        label_palabra.grid(row=1,column=0,padx=20, pady=20, sticky="w",ipady=6)
        fuente=tkFont.Font(family="Arial Rounded MT Bold", size=11, slant="roman")
        label_palabra.configure(font=fuente)

        self.lista_palabra()
        # self.btn_cambiar_direccion = Button(self.ventana,text="Cambiar dirección web ", command=self.cambio_direccion)
        # self.btn_cambiar_direccion.grid(row=1,column=0,padx=20, pady=20, sticky="w",ipady=6)
        
        #Etiqueta de configuracion de dominio
        label_dominio=Label(self.ventana, text="Seleccionar dominio web:")
        label_dominio.grid(row=2,column=0,padx=20, pady=20, sticky="w",ipady=6)
        fuente=tkFont.Font(family="Arial Rounded MT Bold", size=11, slant="roman")
        label_dominio.configure(font=fuente)

        self.lista_dominio()

        # self.btn_cambiar_dominio = Button(self.ventana,text="Cambiar dominio web ", command=self.cambiar_dominio_web)
        # self.btn_cambiar_dominio.grid(row=2,column=0,padx=20, pady=20, sticky="w",ipady=6)
        label_dominio=Label(self.ventana, text=" ")
        label_dominio.grid(row=3,column=0,padx=20, pady=20, sticky="w",ipady=6)
        
        label_dominio=Label(self.ventana, text=" ")
        label_dominio.grid(row=4,column=0,padx=20, pady=20, sticky="w",ipady=6)
        
        btn_agregar=Button(self.ventana,text="Guardar cambios", command=self.guardar_cambios)
        btn_agregar.grid(row=5,column=2,padx=5, pady=6, ipady=4, ipadx=8)
        tip=Hovertip(btn_agregar,'Si desea guardar los cambios realizados a los parámetros del sistema, presione este botón')


        self.ventana.mainloop()


    def guardar_cambios(self):
        print (f"URL seleccionado: {self.combobox1.get()}")
        print (f"Palabra clave seleccionada: {self.combobox2.get()}")
        print (f"Dominio seleccionado: {self.combobox3.get()}")
        
        manipulacion = manipulacion_db()
        manipulacion.editar_url_usado(self.combobox1.get())
        manipulacion.editar_palabra_usada(self.combobox2.get())
        manipulacion.editar_dominio_usado(self.combobox3.get())
        
        
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
        self.tip=Hovertip(self.combobox1,'Puede seleccionar un link de la lista o agregar uno nuevo')

        self.combobox1.grid(row=0, column=1)
        fuente=tkFont.Font(family="Arial", size=10)
        self.combobox1.configure(font=fuente)

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
        self.tip=Hovertip(self.combobox3,'Puede seleccionar un dominio de la lista o agregar uno nuevo')

        fuente=tkFont.Font(family="Arial", size=10)
        self.combobox3.configure(font=fuente)
        self.combobox3.grid(row=2, column=1)
        self.img_boton = tk.PhotoImage(file="agregar.png")
        self.boton3=ttk.Button(self.ventana, image=self.img_boton, command=lambda:[self.cambiar_dominio_web()])
        self.boton3.grid(row=2, column=2,padx=5, pady=6, ipady=2, ipadx=2)  
        tip=Hovertip(self.boton3,'Si desea agregar un nuevo dominio web, presione este botón')

        
        
    # Evento clic botón cambiar dirección web
    def cambio_direccion(self):
        liga= StringVar()
        manipulacion = manipulacion_db()   
        nva_link=Entry(self.ventana,bg="white",textvariable=liga)
        nva_link.grid(row=0,column=3,padx=1, pady=4, ipadx=20,ipady=3)
        fuente=tkFont.Font(family="Arial", size=10)
        nva_link.configure(font=fuente)

        btn_guardar=Button(self.ventana,text="Guardar",command=lambda:[nva_link.destroy(),btn_guardar.destroy(),manipulacion.insertar_cambio_direccion(liga.get()), self.lista_links()])
        btn_guardar.grid(row=0,column=4,padx=5, pady=6, ipady=4, ipadx=8)
        tip=Hovertip(btn_guardar,'Si desea guardar el nuevo registro que introdujo, presione este botón')



    # Evento clic botón cambiar dominio web
    def cambiar_dominio_web(self):
        dominio= StringVar()
        manipulacion = manipulacion_db()   
        nva_dominio=Entry(self.ventana,bg="white",textvariable=dominio)
        nva_dominio.grid(row=2,column=3,padx=1, pady=4, ipadx=20,ipady=3) 
        fuente=tkFont.Font(family="Arial", size=10)
        nva_dominio.configure(font=fuente)

        btn_guardar=Button(self.ventana,text="Guardar",command=lambda:[nva_dominio.destroy(),btn_guardar.destroy(),manipulacion.insertar_cambio_dominio(dominio.get()), self.lista_dominio()])
        btn_guardar.grid(row=2,column=4,padx=5, pady=6, ipady=4, ipadx=8)
        tip=Hovertip(btn_guardar,'Si desea guardar el nuevo registro que introdujo, presione este botón')

        

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
        self.tip=Hovertip(self.combobox2,'Puede seleccionar una palabra de la lista o agregar una nueva')
        fuente=tkFont.Font(family="Arial", size=10)
        self.combobox2.configure(font=fuente)

        self.combobox2.grid(row=1, column=1 )
        self.img_boton2 = tk.PhotoImage(file="agregar.png")
        self.boton2=ttk.Button(self.ventana, image=self.img_boton2, command=lambda:[self.agregar_palabra()])
        self.boton2.grid(row=1, column=2,padx=5, pady=6, ipady=2, ipadx=2) 
        self.tip=Hovertip(self.boton2,'Si desea agregar una nueva palabra, presione este botón')


    def aparecer_lista2(self):
        opcion=tk.StringVar()
        links = self.urlist
        combo = ttk.Combobox(self.ventana, 
                                    width=10, 
                                    textvariable=opcion, 
                                    values=links)
        combo.grid(row=1,column=3,padx=1, pady=6)

        combo.current(0)
        fuente=tkFont.Font(family="Arial", size=10)
        combo.configure(font=fuente)
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
        fuente=tkFont.Font(family="Arial", size=10)
        nva_palabra.configure(font=fuente)

        btn_confirmar=Button(self.ventana,text="Guardar", command=lambda:[nva_palabra.destroy(), btn_confirmar.destroy(), manipulacion.insertar_palabra_nueva(palabra.get()), self.lista_palabra()])
        btn_confirmar.grid(row=1,column=4,padx=1, pady=6, ipady=4, ipadx=8)
        tip=Hovertip(btn_confirmar,'Si desea guardar la nueva palabra que introdujo, presione este botón')



  