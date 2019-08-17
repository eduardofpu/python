user = raw_input('digite o nome do usuario: ')
if user == 'root':
    print 'Usuario logado como , %s'% user
elif user == 'admin':   
 print 'Usuario logado como , %s utilizando o elif'% user 
else:
    print 'Usuario incorreto'    