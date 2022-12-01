from Base_datos_scrapper import conexion_bd
# from extraccion_dof import extraccion

class manipulacion_db():
    '''
    clase de weber dao
    '''
        
    def consulta_links(self, lst_nva_pub, cont_link_dominio, lst_link_dominio):
        '''
        Función que hace la consulta de los links existentes en la Base de datos
        '''
        # print ("entro en consulta link")
        conexion = conexion_bd()  
        conexion.cursor.execute("SELECT * FROM `extraccion` WHERE link = %s;", (lst_link_dominio[cont_link_dominio],))
        self.valores = conexion.cursor.fetchall()
            # Si no encuentra coincidencia del link en la base de datos se considera nueva y se almacena en una nueva lista
        if bool(self.valores) == False:
                lst_nva_pub.append(lst_link_dominio[cont_link_dominio])
                print("paso en if de consulta de link")
        conexion.close_connection() 
        
        return lst_nva_pub
            

    def insertar_links(self, lst_nva_pub, today, cont_liga):
        '''
        Función que inserta los link nuevos a la Base de datos
        '''
        self.lst_nva_pub = lst_nva_pub
        self.today = today
        self.cont_liga = cont_liga
        conexion = conexion_bd()  
        print("Entro en insertar link")
        conexion.cursor.execute("INSERT INTO `extraccion` (`id`, `link`, `fecha`) VALUES (NULL,%(liga)s, %(fecha_actual)s)",{"liga":self.lst_nva_pub[self.cont_liga],"fecha_actual":self.today}) 
        print("estoy aqui")
        print("link= "+self.lst_nva_pub[self.cont_liga])
        conexion.commit_connection()
        conexion.close_connection()
        

    def contrasena_correo(self):
        '''
        Función para obtener la contraseña del correo segun el usuario
        '''
        user = "Eduin nasa"
        self.conexion = conexion_bd()
        self.conexion.cursor.execute("SELECT contraseña FROM `contraseña_correo` WHERE nombre_cuenta = %s; ", (user,))
        contraseña = self.conexion.cursor.fetchall()
        res = [str(x) for x in contraseña]
        chars = "('),"
        nvo_contraseña = ''.join( x for x in res if x not in chars)
        
        nvo_contraseña = ''.join( x for x in nvo_contraseña if x not in chars)
        self.conexion.close_connection()
        
        return nvo_contraseña



    def consulta(conexion):
        '''
        funcion consulta 1 
        '''
        conexion = conexion_bd() 
        conexion.cursor.execute("SELECT `palabra` from lista_palabras;")
        wordlist = conexion.cursor.fetchall()
        conexion.cursor.close()
        conexion.close_connection()
        return wordlist


    def insertar_palabra_nueva(self, palabra):
        self.palabra = palabra
        conexion = conexion_bd()
        conexion.cursor.execute("INSERT INTO `lista_palabras` (`id`, `palabra`) VALUES (NULL,%(word)s)",{"word":self.palabra}) 
        print (self.palabra)
        conexion.commit_connection()
        conexion.close_connection()
        


    def eliminar_palabra(self, palabra):
        self.palabra = palabra
        conexion = conexion_bd()
        conexion.cursor.execute("DELETE FROM `lista_palabras` WHERE `lista_palabras`.`palabra` = (%(word)s)",{"word":self.palabra}) 
        print ("Se eliminó correctamente la palabra: "+self.palabra)
        conexion.close_connection()
        

    def consulta2(conexion):
        '''
        funcion consulta2
        '''
        conexion = conexion_bd() 
        conexion.cursor.execute("SELECT `link` from cambio_link;")
        wordlist = conexion.cursor.fetchall()
        
        conexion.cursor.close()
        conexion.close_connection()
        return wordlist


    def insertar_cambio_direccion(self, direccion):
        '''
        cambio dir
        '''
        self.direccion = direccion
        conexion = conexion_bd()
        conexion.cursor.execute("INSERT INTO `cambio_link` (`id`, `link`) VALUES (NULL,%(liga)s)",{"liga":self.direccion}) 
        print (self.direccion)
        conexion.commit_connection()
        conexion.close_connection()


    def eliminar_direccion(self, direccion):
        self.direccion = direccion
        conexion = conexion_bd()
        conexion.cursor.execute("DELETE FROM `cambio_link` WHERE `cambio_link`.`link` = (%(url)s)",{"url":self.direccion}) 
        print ("Se eliminó correctamente la dirección: "+self.direccion)
        conexion.close_connection()


    def consulta3(conexion):
        conexion = conexion_bd() 
        conexion.cursor.execute("SELECT `dominio` from cambio_dominio;")
        lista_dominios = conexion.cursor.fetchall()
        conexion.cursor.close()
        conexion.close_connection()
        return lista_dominios


    def insertar_cambio_dominio(self, dominio):
        self.dominio = dominio
        conexion = conexion_bd()
        conexion.cursor.execute("INSERT INTO `cambio_dominio` (`id`, `dominio`) VALUES (NULL,%(dominio)s)",{"dominio":self.dominio}) 
        print (self.dominio)
        conexion.commit_connection()
        conexion.close_connection()

    def eliminar_dominio(self, dominio):
        self.dominio = dominio
        conexion = conexion_bd()
        conexion.cursor.execute("DELETE FROM `cambio_dominio` WHERE `cambio_dominio`.`dominio` = (%(domain)s)",{"domain":self.dominio}) 
        print ("Se eliminó correctamente la dirección: "+self.dominio)
        conexion.close_connection()

        '''
        def consulta_link_nuevo(self):
            conexion = conexion_bd()
            conexion.cursor.execute("SELECT `link` FROM `cambio_link` WHERE id = 1;")
            self.valores = conexion.cursor.fetchall()
            print(self.valores)
        '''
    def editar_url_usado(self, url_nuevo):
        self.url_nuevo = url_nuevo
        conexion = conexion_bd()
        conexion.cursor.execute("UPDATE `url_en_uso` SET `url` = %(liga)s WHERE `url_en_uso`.`id` = 1;",{"liga":self.url_nuevo})
        print (self.url_nuevo)
        conexion.commit_connection()
        conexion.close_connection()


    def url_usado():
        conexion = conexion_bd()
        conexion.cursor.execute("SELECT `url` from url_en_uso WHERE id = 1; ")
        url = conexion.cursor.fetchall()
        res = [str(x) for x in url]
        chars = "('),"
        nvo_url = ''.join( x for x in res if x not in chars)
        nvo_url = ''.join( x for x in nvo_url if x not in chars)
        conexion.close_connection()
        return nvo_url

            
    def editar_palabra_usada(self, palabra_nueva):
        self.palabra_nueva = palabra_nueva
        conexion = conexion_bd()
        conexion.cursor.execute("UPDATE `palabra_actual` SET `palabra` = %(palabra)s WHERE `palabra_actual`.`id` = 1;",{"palabra":self.palabra_nueva})
        print (self.palabra_nueva)
        conexion.commit_connection()
        conexion.close_connection()


    def palabra_usada():
        conexion = conexion_bd()
        conexion.cursor.execute("SELECT `palabra` from `palabra_actual` WHERE id = 1; ")
        palabra = conexion.cursor.fetchall()
        res = [str(x) for x in palabra]
        chars = "('),"
        nva_palabra = ''.join( x for x in res if x not in chars)
        nva_palabra = ''.join( x for x in nva_palabra if x not in chars)
        conexion.close_connection()
        return nva_palabra


    def editar_dominio_usado(self, dominio_nuevo):
        self.dominio_nuevo = dominio_nuevo
        conexion = conexion_bd()
        conexion.cursor.execute("UPDATE `dominio_en_uso` SET `dominio` = %(dominio)s WHERE `dominio_en_uso`.`id` = 1;",{"dominio":self.dominio_nuevo})
        print (self.dominio_nuevo)
        conexion.commit_connection()
        conexion.close_connection()


    def dominio_usado():
        conexion = conexion_bd()
        conexion.cursor.execute("SELECT `dominio` from `dominio_en_uso` WHERE id = 1; ")
        dominio = conexion.cursor.fetchall()
        res = [str(x) for x in dominio]
        chars = "('),"
        nvo_dominio = ''.join( x for x in res if x not in chars)
        nvo_dominio = ''.join( x for x in nvo_dominio if x not in chars)
        conexion.close_connection()
        return nvo_dominio
    
    def consulta(conexion):
        conexion = conexion_bd() 
        conexion.cursor.execute("SELECT `palabra` from lista_palabras;")
        wordlist = conexion.cursor.fetchall()
        conexion.cursor.close()
        conexion.close_connection()
        return wordlist
