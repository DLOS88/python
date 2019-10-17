palabra = input('ingrese una palabra: ')
caracter = input('ingrese un caracter: ')

if caracter in palabra:
    print('el caracter (' + caracter + ') esta contenido en ' + palabra)
else:
    print('el caracter (' + caracter + ') No esta contenido')
