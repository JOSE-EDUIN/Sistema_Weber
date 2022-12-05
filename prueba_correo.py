import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from contenido_correo import firma_html

msg = MIMEMultipart('alternative')
msg['Subject'] = 'El asunto del correo es este'
msg['From'] = 'jnahuat@nasa.com.mx'
msg['To'] = 'frester_dui98@hotmail.com'

# html = firma_html()
# cuerpo = MIMEText(html, 'html')
# msg.attach(cuerpo)
mensajes = "Se ha identificado una nueva publicacion referentes al articulo 69-B"
                # links= mensajes, 'plain'
msg.attach(MIMEText(mensajes, 'plain'))
s = smtplib.SMTP('smtp.office365.com', port=587)
s.starttls()
s.login('jnahuat@nasa.com.mx', 'pbfbndlpwngmcdtr')
s.sendmail('jnahuat@nasa.com.mx', ['frester_dui98@hotmail.com'], msg.as_string())
s.quit()