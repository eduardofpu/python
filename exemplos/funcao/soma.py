import glob,os,sys

def entrada():
    x = raw_input('Digite um valora x: ')
    y = raw_input('Digite um valora y: ')
    soma(x,y)

def soma(x,y):    
    total = (int(x) + int(y))
    imprimir(total)
    
def imprimir(total):    
    # print 'A soma de x + y = ' +str(total)
    print('A soma de x + y = % d ' % total)

def main(args):
    entrada()


if __name__ == '__main__':
    sys.exit(main(sys.argv))