import smtplib
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

meu_email = 'x@gmail.com'
encaminhar = 'y@hotmail.com'

# rb e uma leitura binaria
msg = MIMEMultipart()
msg['From'] = meu_email
msg['To'] = encaminhar
msg['Subject'] = 'image mp4'

boby = "Image"
msg.attach(MIMEText(boby))
filename = 'image.mp4'
attachment = open(filename, "rb")



mimetype_anexo = mimetypes.guess_type(filename)[0].split('/')
part = MIMEBase(mimetype_anexo[0], mimetype_anexo[1])


part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(meu_email, open('senha.txt').read().strip())

text = msg.as_string()
print(text)

server.sendmail(meu_email, encaminhar, text)
server.quit()