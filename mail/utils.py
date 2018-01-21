import hashlib
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from email.utils import formataddr

def send_confirmation(from_email, from_pass, to_email , subject='', description='', titulo=''):
    if subject == '':
        titulo = "Registro "
    else:
        titulo = subject

    if description == '':
        description = """Para confirmar su registro de  """
    else:
        description = description
    text = description
    html = """\
    <html>
      <head>
        <title>{}</title>
      </head>
      <body background: #D6D6D5;">
          <div style="background: white; padding: 2% 4% 2%">
            {}
          </div>
      </body>
    </html>
    """.format(titulo, description)
    try:
        #user_ = "infolacarga@gmail.com"
        #pass_ = "20100348"
        #email_to = 'jose.evanan@gmail.com'
        mensaje = MIMEMultipart('alternative')
        text_text = MIMEText(text, "text")
        text_html = MIMEText(html, "html")
        mensaje.attach(text_text)
        mensaje.attach(text_html)
        mensaje['From'] = formataddr(('La-Carga', from_email))
        mensaje['To'] = to_email
        mensaje['Subject'] = "titulo"
        server_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        server_smtp.ehlo()
        server_smtp.starttls()
        server_smtp.ehlo()
        server_smtp.login(from_email, from_pass)
        server_smtp.sendmail(from_email, to_email, mensaje.as_string())
        server_smtp.close()
        return True
    except Exception as error:
        return False
