import smtplib
from email.MIMEText import MIMEText

meu_email = 'x@gmail.com'
encaminhar = ['y@gmail.com','k@hotmail.com']

# rb e uma leitura binaria
msg = MIMEText(open('email.txt','rb').read())
msg['From'] = 'Eduardo R Delfino'
msg['To'] = 'Pythonicos'
msg['Subject'] = 'Enviando Teste'

msg = msg.as_string()
print(msg)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(meu_email, open('senha.txt').read().strip())
server.sendmail(meu_email, encaminhar, msg)
server.quit()