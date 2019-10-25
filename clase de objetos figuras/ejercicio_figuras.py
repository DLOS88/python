from Figuras import *

p1 = Punto_forma(5, 5)
p2 = Punto_forma(9, 10)
cuadrado = Cuadrado_forma(p1, p2)
circulo = Circulo_forma(p1, p2)
rectangulo = Rectangulo_forma(p1, p2)
triangulo = Triangulo_forma(p1, p2)

print('circulo'+ str(circulo))

cuadrado.calcular_area()
cuadrado.calcular_perimetro()
circulo.calcular_area()
circulo.calcular_perimetro()
rectangulo.calcular_area()
rectangulo.calcular_perimetro()
triangulo.calcular_area()
triangulo.calcular_perimetro()

print('area del cuadrado es: '+ str(cuadrado.area))
print('perimetro del cuadrado es: '+ str(cuadrado.perimetro))
print('area del circulo es: '+ str(circulo.area))
print('perimetro del circulo es: '+ str(circulo.perimetro))
print('area del rectangulo es: '+ str(rectangulo.area))
print('perimetro del rectangulo es: '+ str(rectangulo.perimetro))
print('area del triangulo es: '+ str(triangulo.area))
print('perimetro del triangulo es: '+ str(triangulo.perimetro))
