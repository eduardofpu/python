import sys
# var = list()
# for x in range(1,11):
#     var.append(x)
# print var  

var = sys.version_info.list()
valor = raw_input('Digite um valor: ')
entrada = int(valor)
for x in range(1,entrada):
    var.append(x)
print(var)