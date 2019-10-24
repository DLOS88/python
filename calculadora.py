from operaciones import *

#con el import * es como si se hubieran declarado todas las funciones de ese modulo

n1 = int(input('ingrese un numero: '))
n2 = int(input('ingrese otro numero: '))

print('suma(' + str(n1) + ' , ' + str(n2) + ') = ' + str(suma(n1, n2)))
print('resta(' + str(n1) + ' , ' + str(n2) + ') = ' + str(resta(n1, n2)))
print('multiplicar(' + str(n1) + ' , ' + str(n2) + ') = ' + str(multiplicacion(n1, n2)))
print('dividir(' + str(n1) + ' , ' + str(n2) + ') = ' + str(dividir(n1, n2)))
