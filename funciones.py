def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def mayor(n1, n2):
    if n1 > n2:
        return n1 
    if n1 < n2:
        return n2

def operacion(n1, n2):
    n1, n2 = n2 , n1
    print(n1, n2)
'''
n1 = int(input('Ingrese un numero: '))
n2 = int(input('Ingrese otro numero: '))

if mayor(n1, n2):
    print(resta(n1, n2))
else:
    print(suma(5, 6))

operacion(n1, n2)
print(n1, n2)'''


n = int(input('Ingrese un numero: '))
def fibo (n):
    if n in [0,1]:
        return 1
    return fibo(n-1) + fibo(n-2)

for i in range(0,n):
    print('fibo(' + str(i) + ') = ' + str(fibo(i)))

def fibo2(n):
    lista = []
    if n==1:
         lista.append(1)
    else:
        if n==2:
        lista.append(1)
        lista.append(1)
    elif n>2:
        print(str(lista(0)))
        for i in range (2,n):
            print('dato: ' + str(lista(i-1)))
            lista.append(lista(i-1)+lista(i-2))
    return lista
fibo2(n)
        
