import smtplib

#Email recipiente
meu_email = "x@gmail.com"

#Email destinatario
enviar_para = "y@hotmail.com"

#servidor SMTP
smtp = "smtp.gmail.com"

#Servidor SMTP
server = smtplib.SMTP(smtp,587)

#Define conexoes usando tls
server.starttls()

#Realiza login no servidor de SMTP passando usuario e senha
server.login(meu_email, open('senha.txt').read().strip())


#Corpo do email
msg = '''
      Envio de e-mail teste
      Curoso Phytonicos
      Bem-vindo a aula de envio de e-mail

'''
#Enviar o email
server.sendmail(meu_email, enviar_para, msg)

#Fechar a conexao
server.quit()