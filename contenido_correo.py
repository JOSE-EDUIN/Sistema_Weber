from email.message import EmailMessage

 

def msg_publicacion_html():
    html = """\
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Correo electronico</title>
            </head>
            <body>
                <p><b>
                    <FONT SIZE=7, COLOR=#00FF00>Se ha identificado una nueva publicación, abra el contenido del archivo de texto:  </FONT>
                </b></p>
                
            </body>
        </html>
    """
     
    return html

def msg_no_publicacion_html():
    html2 = """\
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Correo electronico</title>
            </head>
            <body>
                <p><b>
                    <FONT SIZE=7, COLOR=#FF0000>No se identificó ninguna notificación en el Diario Oficial de la Federación  </FONT>
                </b></p>
                
            </body>
        </html>
    """
     
    return html2

def msg_error_html():
    html3 = """\
        <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Correo electronico</title>
            </head>
            <body>
                <p><b>
                    <FONT SIZE=7, COLOR=#FF0000>El proceso de consulta terminó con errores, revise el monitoreo de Weber.  </FONT>
                </b></p>
                
            </body>
        </html>
    """
    return html3