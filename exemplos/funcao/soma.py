import glob,os,sys

def entrada():
    x = input('Digite um valora x: ')
    y = input('Digite um valora y: ')
    soma(x,y)

def soma(x,y):    
    total = (int(x) + int(y))
    imprimir(total)
    
def imprimir(total):    
    # print 'A soma de x + y = ' +str(total)
    print('A soma de x + y = % d ' % total)

def main():
    entrada()


if __name__ == '__main__':
    main()