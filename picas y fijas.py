import random

long = int(input('ingrese la longitud del numero: '))
numero=[]

#len es una funcion que me entrega la longitud de la lista
while len(numero) < long:
    digito = random.randint(0,9)
    if digito not in numero:
        #lista.append(d), se agrega d a la lista
        numero.append(digito)

print(numero)

fijas=0

while fijas != long:
    picas=0
    fijas=0
    while True:
        usuario=[]
        while True:
            intento = input('ingrese un numero: ')
            if len(intento)!=long:
                print('El numero ingresado tiene una longitud diferente de la inicial')
            else:
                break

        for i in intento:
            if int(i) not in usuario:
                usuario.append(int(i))
        if len(usuario) == long:
            break
        else:
            print('Numero no valido')
            
    print (numero,usuario)

    for i  in range(0,long):
        if usuario[i] in numero:
            if usuario[i] == numero[i]:
                fijas+=1
            else:
                picas+=1
            
    print('p: ' + str(picas) + ', f: ' + str(fijas) )        



