
def centrar_pantalla(gui, altura, ancho):
    '''
    Función para posicionar la pantalla en el centro
    '''
    #  Obtenemos el largo y  ancho de la pantalla
    wtotal = gui.winfo_screenwidth()
    htotal = gui.winfo_screenheight()

    #  Guardamos el alto y largo de la ventana
    hventana = altura # 500
    wventana = ancho # 700
    

    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)

    #  Se lo aplicamos a la geometría de la ventana
    gui.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
    