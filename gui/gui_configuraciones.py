from tkinter import *
import tkinter as tk
from tkinter import ttk
from idlelib.tooltip import Hovertip
import tkinter.font as tkFont
from extraccion_dof import *
from weber_dao import manipulacion_db
from centrarPantalla import centrar_pantalla
from tkinter import messagebox

    
class configuracion():
    
    def __init__(self):
        '''
        clase de configuracion 
        
        '''
        # self.ventana_padre = gui
        self.dato=""       
        self.ventana = Toplevel()
        self.ventana.title("Sistema Weber: Configuración")
        self.ventana.iconbitmap("img/weberIcon.ico")
        centrar_pantalla(self.ventana, 350, 725)
        ## Provoca que la ventana tome el focus
        self.ventana.focus_set()
        ## Deshabilita todas las otras ventanas hasta que esta ventana sea destruida.
        self.ventana.grab_set()
    
        # Establecimiento de la conexión a la base de datos
        self.manipulacion = manipulacion_db()
        manipulacion2 = manipulacion_db()
        self.urlist = manipulacion2.consulta2()
        self.fuente=tkFont.Font(family="Arial Rounded MT Bold", size=11, slant="roman")
        self.fuente_secundaria=tkFont.Font(family="Arial Rounded MT Bold", size=9, slant="roman")
        self.img_boton3 = tk.PhotoImage(file="img/agregar.png")
        self.img_boton_confirmar = tk.PhotoImage(file="img/confirmar.png")
        self.img_boton_cancelar = tk.PhotoImage(file="img/cancelar.png")
        
        #Etiquetas de configuracion url
        label_url = Label(self.ventana, text="Seleccionar URL: ")
        label_url.grid(row=0 ,column=0,padx=20, pady=20, sticky="w",ipady=6)
        label_url.configure(font=self.fuente)
        
        self.lista_links()
        
        self.img_boton1 = tk.PhotoImage(file="img/agregar.png")
        btn_agregar1=ttk.Button(self.ventana,image=self.img_boton1, command=self.cambio_direccion)
        btn_agregar1.grid(row=0,column=2,padx=8, pady=3,sticky="w")
        tip=Hovertip(btn_agregar1,'Si desea agregar una nueva dirección web, presione este botón')
        
        self.img_boton2 = tk.PhotoImage(file="img/eliminar.png")
        btn_eliminar1=ttk.Button(self.ventana,image=self.img_boton2, command=self.eliminar_url)
        btn_eliminar1.grid(row=0,column=3, pady=3,sticky="w")
        tip=Hovertip(btn_eliminar1,'Si desea eliminar una dirección web, presione este botón')
       
        #Etiquetas de configuracion palabra clave
        label_palabra = Label(self.ventana, text="Seleccionar palabra clave: ")
        label_palabra.grid(row=2,column=0,padx=20, pady=20, sticky="w",ipady=6)
        fuente=tkFont.Font(family="Arial Rounded MT Bold", size=11, slant="roman")
        label_palabra.configure(font=fuente)

        self.lista_palabra()
        
       
        self.boton2=ttk.Button(self.ventana, image=self.img_boton3, command=self.agregar_palabra)
        self.boton2.grid(row=2, column=2,padx=8, pady=3,sticky="w") 
        self.tip=Hovertip(self.boton2,'Si desea agregar una nueva palabra, presione este botón')
        
        self.img_boton4 = tk.PhotoImage(file="img/eliminar.png")
        btn_eliminar2=ttk.Button(self.ventana,image=self.img_boton4, command=self.eliminar_palabra_clave)
        btn_eliminar2.grid(row=2,column=3, pady=3,sticky="w")
        tip=Hovertip(btn_eliminar2,'Si desea eliminar una dirección web, presione este botón')
        
        #Etiqueta de configuracion de dominio
        label_dominio=Label(self.ventana, text="Seleccionar dominio web:")
        label_dominio.grid(row=4,column=0,padx=20, pady=20, sticky="w",ipady=6)
        # fuente=tkFont.Font(family="Arial Rounded MT Bold", size=11, slant="roman")
        label_dominio.configure(font=self.fuente)

        self.lista_dominio()
        
        self.img_boton5 = tk.PhotoImage(file="img/agregar.png")
        self.boton3=ttk.Button(self.ventana, image=self.img_boton5, command=self.cambiar_dominio_web)
        self.boton3.grid(row=4, column=2,padx=8, pady=3,sticky="w")  
        tip=Hovertip(self.boton3,'Si desea agregar un nuevo dominio web, presione este botón')
        
        self.img_boton6 = tk.PhotoImage(file="img/eliminar.png")
        btn_eliminar3=ttk.Button(self.ventana,image=self.img_boton6, command=self.eliminar_dominio_web)
        btn_eliminar3.grid(row=4,column=3, pady=3,sticky="w")
        tip=Hovertip(btn_eliminar3,'Si desea eliminar una dirección web, presione este botón')
        
        
        
        
                
        # label_espacio2=Label(self.ventana, text=" ")
        # label_espacio2.grid(row=6,column=0)
        
        frame_botones_final = ttk.Frame(self.ventana, width=500, height=50)
        frame_botones_final.grid(row=7,column=1)
        
        btn_cancelar=Button(frame_botones_final,text="Cancelar", command=self.cancelar)
        btn_cancelar.grid(row=0,column=0, padx=10, pady=6, ipady=4, ipadx=8)
        tip=Hovertip(btn_cancelar,'Si desea cancelar los cambios realizados a los parámetros del sistema, presione este botón')

        btn_agregar=Button(frame_botones_final,text="Guardar cambios", command=self.guardar_cambios)
        btn_agregar.grid(row=0,column=1, padx=10, pady=6, ipady=4, ipadx=8)
        tip=Hovertip(btn_agregar,'Si desea guardar los cambios realizados a los parámetros del sistema, presione este botón')
                
        self.ventana.mainloop()


    def eliminar_url(self):
        '''
        Elimina url en la lista
        '''
        # manipulacion = manipulacion_db()
        self.manipulacion.eliminar_direccion(self.combobox1.get())
        self.lista_links()

    
    def eliminar_palabra_clave(self):
        '''
        Elimina palabra clave 
        '''
        # manipulacion = manipulacion_db()
        self.manipulacion.eliminar_palabra(self.combobox2.get())
        self.lista_palabra()


    def eliminar_dominio_web(self):
        '''
        Elimina dominio web
        '''
        # manipulacion = manipulacion_db()
        self.manipulacion.eliminar_dominio(self.combobox3.get())
        self.lista_dominio()
    
    
    def cancelar(self):
        self.ventana.destroy()
        
    
    def check_url(self, liga):
        self.dato = liga.get()
        manipulacion = manipulacion_db()
        if self.dato.isspace():
            print("ingrese algo mas largo")
        # else:
        #     manipulacion.insertar_cambio_direccion(self.dato)
        #     self.lista_links()
        
        
    def guardar_cambios(self):
        print (f"URL seleccionado: {self.combobox1.get()}")
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
        print(links)
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
        self.combobox3.grid(row=4, column=1)

        
        
    # Evento clic botón cambiar dirección web
    def cambio_direccion(self):
        liga= StringVar()
        manipulacion = manipulacion_db()   
        label_nueva_url=Label(self.ventana, text="Agregue nueva url: ")
        label_nueva_url.grid(row=1,column=0,padx=20, pady=20, sticky="w",ipady=6)
        label_nueva_url.configure(font=self.fuente_secundaria)
        self.nva_link=Entry(self.ventana,bg="white",textvariable=liga)
        self.nva_link.grid(row=1,column=1,padx=1, pady=4, ipadx=20,ipady=3, sticky=W)
        fuente=tkFont.Font(family="Arial", size=10)
        self.nva_link.configure(font=fuente)

        btn_guardar=ttk.Button(self.ventana, image=self.img_boton_confirmar, command=lambda:[btn_cancelar.destroy(), self.nva_link.destroy(), label_nueva_url.destroy(), btn_guardar.destroy(),manipulacion.insertar_cambio_direccion(liga.get()), self.lista_links()])
        btn_guardar.grid(row=1,column=2,padx=8, pady=3,sticky="w")
        btn_cancelar=ttk.Button(self.ventana, image=self.img_boton_cancelar, command=lambda:[self.nva_link.destroy(), label_nueva_url.destroy(), btn_cancelar.destroy(), btn_guardar.destroy()])
        btn_cancelar.grid(row=1,column=3,pady=3,sticky="w")
        tip=Hovertip(btn_guardar,'Si desea guardar el nuevo registro que introdujo, presione este botón')
        tip=Hovertip(btn_cancelar,'Si desea cancelar la acción, presione este botón')



    # Evento clic botón cambiar dominio web
    def cambiar_dominio_web(self):
        dominio= StringVar()
        manipulacion = manipulacion_db()   
        label_nueva_dominio=Label(self.ventana, text="Agregue nuevo dominio: ")
        label_nueva_dominio.grid(row=5,column=0,padx=20, pady=20, sticky="w",ipady=6)
        label_nueva_dominio.configure(font=self.fuente_secundaria)
        nva_dominio=Entry(self.ventana,bg="white",textvariable=dominio)
        nva_dominio.grid(row=5,column=1,padx=1, pady=4, ipadx=20,ipady=3, sticky="w") 
        fuente=tkFont.Font(family="Arial", size=10)
        nva_dominio.configure(font=fuente)

        btn_guardar=ttk.Button(self.ventana, image=self.img_boton_confirmar, command=lambda:[btn_cancelar.destroy(), label_nueva_dominio.destroy(), nva_dominio.destroy(),btn_guardar.destroy(),manipulacion.insertar_cambio_dominio(dominio.get()), self.lista_dominio()])
        btn_guardar.grid(row=5,column=2,padx=8, pady=3,sticky="w")
        btn_cancelar=ttk.Button(self.ventana, image=self.img_boton_cancelar, command=lambda:[nva_dominio.destroy(),btn_guardar.destroy(),btn_cancelar.destroy(), label_nueva_dominio.destroy()])
        btn_cancelar.grid(row=5,column=3,pady=3,sticky="w")
        tip=Hovertip(btn_guardar,'Si desea guardar el nuevo registro que introdujo, presione este botón')
        tip=Hovertip(btn_cancelar,'Si desea cancelar la acción, presione este botón')

        

    # Evento botón aparecer lista de palabras
    def lista_palabra(self):
        '''
        muestra la lista de palabras en la bd
        '''
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
        self.combobox2.grid(row=2, column=1 )
        

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
        '''
        Funcion para agregar la palabra clave en la base de datos
        '''
        palabra= StringVar()
        manipulacion = manipulacion_db()
        label_nueva_palabra=Label(self.ventana, text="Agregue nueva palabra: ")
        label_nueva_palabra.grid(row=3,column=0,padx=20, pady=20, sticky="w",ipady=6)
        label_nueva_palabra.configure(font=self.fuente_secundaria)
        nva_palabra = Entry(self.ventana, bg="white", textvariable=palabra)
        nva_palabra.grid(row=3,column=1,padx=1, pady=6, ipady=4, ipadx=8, sticky="w")
        fuente=tkFont.Font(family="Arial", size=10)
        nva_palabra.configure(font=fuente)

        btn_guardar=ttk.Button(self.ventana, image=self.img_boton_confirmar, command=lambda:[btn_cancelar.destroy(), label_nueva_palabra.destroy(), nva_palabra.destroy(), btn_guardar.destroy(), manipulacion.insertar_palabra_nueva(palabra.get()), self.lista_palabra()])
        btn_guardar.grid(row=3,column=2,padx=8, pady=3,sticky="w")
        btn_cancelar=ttk.Button(self.ventana, image=self.img_boton_cancelar, command=lambda:[label_nueva_palabra.destroy(), nva_palabra.destroy(), btn_cancelar.destroy(), btn_guardar.destroy()])
        btn_cancelar.grid(row=3,column=3,pady=3,sticky="w")
        tip=Hovertip(btn_guardar,'Si desea guardar la nueva palabra que introdujo, presione este botón')
        tip=Hovertip(btn_cancelar,'Si desea cancelar la acción, presione este botón')


  