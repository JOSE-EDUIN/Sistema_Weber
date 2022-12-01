from ast import Try
from weber_dao import manipulacion_db
from gui.pruebaframe import frame_monitoreo
import urllib.request
from datetime import datetime
from msilib.schema import Property
from bs4 import BeautifulSoup
import re 
from Base_datos_scrapper import conexion_bd

'''
    importamos para envios de correos
'''
import smtplib 
from email.message import EmailMessage 


'''
Documentar el código
try para errores de importacion 
archivo de requeriments 
agregar los self 
eliminar lineas inecesarias
documentar metodos 
asignar nombres de variables relacionadas a su funcion 
nombre de clase empieza en mayuscula
globales en mayusculas
uso de propiedades
nombre de los archivos 
formato de los snake case 
dos saltos de linea en cada def
'''


class extraccion():
    '''
    Clase que se utiliza para la extraccion de los links de la página del DOF
    '''
    def __init__(self):
       self.lst_nva_pub2=[]
       self.monitoreo = frame_monitoreo()
       self.manipulacionDb = manipulacion_db()

    def acceso_web(self):
        '''
        Función que establece la conexion con la página,
        leerá y decodificará la página 
        '''
        
        try:
            url1 = manipulacion_db.url_usado()
            print("Url1= "+url1)
            self.datos = urllib.request.urlopen(url1).read().decode()
            # self.datos = urllib.request.urlopen("https://www.dof.gob.mx/index_111.php?year=2022&month=10&day=11#gsc.tab=0").read().decode()
               
        except urllib.error.URLError as e:
            self.monitoreo.gif_error_web()
            print(f"Error al intentar acceder a la pagina web: {e}")
            # print("cosa por error web")
            
        else:
            print("Conexión a la página web establecida")
            self.monitoreo.gif_cargando()
            
    
    def conn_bd(self):
        '''
        Funcion para llamar la conexion a la bd
        '''
        try:
            self.conn_bd = conexion_bd()
        except:
            self.monitoreo.gif_error_bd()
            print("error en establecer conexion bd en dof")
        else:
            print("conexion bd en dof")
            self.monitoreo.gif_cargando2()
        
    def buscar_69b(self):
        '''
        Función para transformar todo el HTML en un objeto de Beautiful Soup,
        busca dentro de las etiquetas la palabra clave y hace un conteo de las veces que aparece
        
        '''
        try:
            
            self.soup = BeautifulSoup(self.datos, 'lxml')
            self.box = self.soup.find('tr',id="trcontent")
            self.resultado = self.box.find_all('a',class_='enlaces')
            self.palabra = re.findall(r'69-B', str(self.resultado))
            
            print(self.palabra)
            
            #Contar elementos
            self.transforma = ", ".join(map(str, self.palabra))
            self.conteo = len(self.transforma.split())
        except:
            self.monitoreo.gif_error_busqueda_publicacion()
            print("Error en busqueda de palabra clave")
        else:
            print("Buscando palabra clave")
            self.monitoreo.gif_cargando3()
            
            
        
    def obtener_link(self):
        '''
        Función que recupera los links de las las publicaciones donde se encuentre la palabra
        clave
        '''
        
        try:
            #Recupera todos los link de las publicaciones y las almacena en una lista -links[]
            self.lst_links =[]
            self.lst_69B =[]
            lst_link_dominio =[]
            x=0
            
            for ref in self.resultado:
                tag=ref.get('href')+'\n'
                transforma="".join(map(str, tag))
                link=[transforma.split('\n')]
                self.lst_links.append(link)
                
            #Resguarda especialmente los links en donde se encuentre la palabra 69-B en una lista -lst_69B[]        
            for Pos_info in self.resultado:
                encuentra = re.findall(r'69-B', str(Pos_info))
                if bool(encuentra)==True:
                    PosLink = self.lst_links[x]
                    self.lst_69B.append(PosLink)
                
                x+=1

            #Elimina carcateres innecesarios de los links y las concatena con el dominio de la pagina 
            for Textlink in self.lst_69B:
                cadena = Textlink[0]
                characters = "[]'"
                cadena = ''.join( x for x in cadena if x not in characters)
                cal='https://www.dof.gob.mx'+cadena
                lst_link_dominio.append(cal)
                print(cal)
            
            
        except:
            self.monitoreo.gif_error_extraer_link()
            print("Error al extraer links")
            
        else:
            print ("Extrayendo links de publicaciones realizada")
            self.monitoreo.gif_cargando4()    
            return lst_link_dominio    

    def fecha_actual(self):
        '''
        Función para obtener la fecha actual
        '''
        today = datetime.now()
        
        return today
      
      
    def validar_pub_nva(self):
        '''
        Función que valida si los links encontrados no se encuentran en la base de datos y 
        sean considerados como nuevas publicaciones
        '''
        try:
            
            # Validar si la publiacion es nueva o ya ha sido almacenada en la base de datos
            self.cont_link_dominio = 0
            self.lst_nva_pub = []
            self.cont_lig = 0
            lst_link_dominio = self.obtener_link()
            # lst_nva_pub2 = []
            for ciclo in range(self.conteo):
                
                self.lst_nva_pub2 = self.manipulacionDb.consulta_links(self.lst_nva_pub, self.cont_link_dominio, lst_link_dominio)
                self.cont_link_dominio+=1
            
            #Insercion de valores en la base de datos
            for ciclo in self.lst_nva_pub2:
                self.manipulacionDb.insertar_links(self.lst_nva_pub2, self.fecha_actual(), self.cont_lig)
                self.cont_lig+=1
            
            # Convertimos la lista de los links nuevos en cadena de texto
            self.str_pubs_nva = ", \n ".join(self.lst_nva_pub2)
        except:
            self.monitoreo.gif_error_enviar_link()
            print("Error al intentar insertar el link")            
        else:
            print("Links enviados a la base de datos")
            self.monitoreo.gif_cargando5()

    def notificacion_correo(self):
        '''
        Función que envia notificacion por correo electronico 
        cuando termina de realizar la consulta en la página del DOF
        '''
        self.asunto_correo = "Publicaciones del Diario Oficial de la Federación" 
        # self.correo_remitente = "frester_dui98@hotmail.com" 
        self.correo_remitente = "jnahuat@nasa.com.mx"
        # self.correo_receptor = "oaguilar@nasa.com.mx"
        self.correo_receptor = "frester_dui98@hotmail.com"
        self.email_smtp = "smtp.office365.com" 
        self.contrasena_correo = self.manipulacionDb.contrasena_correo()
        # self.contrasena_correo = "pbfbndlpwngmcdtr" #contraseña aplicacion Nasa
        # self.contrasena_correo = "poykyzptkdiihjhe" #contraseña aplicacion hotmail frester
        
        self.mensaje = EmailMessage() 
        self.mensaje['Subject'] = self.asunto_correo 
        self.mensaje['From'] = self.correo_remitente 
        self.mensaje['To'] = self.correo_receptor
        print(self.contrasena_correo)
        try:
                    
            if bool(self.lst_nva_pub2) == True:
                print(f"Se ha identificado una nueva publicación referente al artículo 69-B: \n{self.str_pubs_nva}")
                self.mensaje.set_content(f"Se ha identificado una nueva publicación referente al artículo 69-B: \n{self.str_pubs_nva}") 

                    # smtp servidor y puerto 
                server = smtplib.SMTP('smtp.office365.com', port=587) 
                server.ehlo() 
                server.starttls() 
                print("Conectando al sservidor SMTP")
                server.login(self.correo_remitente, self.contrasena_correo) 
                server.send_message(self.mensaje) 
                server.quit()


            if bool(self.lst_nva_pub2) == False:
                print("No se ha encontrado publicación nueva referente al articulo 69-B")
                self.mensaje.set_content("No se ha encontrado publicación nueva referente al articulo 69-B") 

                server = smtplib.SMTP('smtp.office365.com', port=587)  
                server.ehlo() 
                server.starttls() 
                print("Conectando al servidor SMTP")
                server.login(self.correo_remitente, self.contrasena_correo) 
                server.send_message(self.mensaje) 
                server.quit()
                    
        except smtplib.SMTPException as e:
            self.monitoreo.gif_error_envio_correo()
            print ('Error al intentar enviar el correo electronico, cuasa del error: ', e)
        else:
            print('Correo electronico enviado con exito')
            self.monitoreo.gif_cargando6()