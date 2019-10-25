from punto import *
from math import pi

class Figura:

    def __init__(self, p1, p2):
        self.origen = p1
        self.destino = p2
        self.area = 0
        self.perimetro = 0

    def calculo_punto(self, p1, p2):
        p3 = Punto_forma(p1.x, p2.y)
        return p3


    def calculo_lado(self, p1, p2):   
        lado = p1.calcular_distancia(p2)
        return lado

class Cuadrado_forma(Figura):

    def calcular_area(self):
        lado = self.calculo_lado(self.origen,self.destino)
        self.area = lado * lado
        
    def calcular_perimetro(self):
        lado = self.calculo_lado(self.origen,self.destino)
        self.perimetro = 4 * lado

class Circulo_forma(Figura):

    def calcular_area(self):
        radio = self.calculo_lado(self.origen,self.destino)
        self.area = pi * (radio ** 2)

    def calcular_perimetro(self):
        radio = self.calculo_lado(self.origen,self.destino)
        self.perimetro = 2 * pi * radio

    
    
    

class Rectangulo_forma(Figura):


    def calcular_area(self):
        p3 = self.calculo_punto(self.origen, self.destino)
        lado1 = self.calculo_lado(p3,self.destino)
        lado2 = self.calculo_lado(self.origen, p3)
        self.area = lado1 * lado2
        
    def calcular_perimetro(self):
        p3 = self.calculo_punto(self.origen, self.destino)
        lado1 = self.calculo_lado(p3,self.destino)
        lado2 = self.calculo_lado(self.origen, p3)
        self.perimetro = 2 * (lado1 + lado2)


class Triangulo_forma(Figura):


    def calcular_area(self):
        p3 = self.calculo_punto(self.origen, self.destino)
        lado1 = self.calculo_lado(p3,self.destino)
        lado2 = self.calculo_lado(self.origen, p3)
        self.area = lado1 * lado2 / 2
        
    def calcular_perimetro(self):
        p3 = self.calculo_punto(self.origen, self.destino)
        lado1 = self.calculo_lado(p3,self.destino)
        lado2 = self.calculo_lado(self.origen, p3)
        lado3 = self.calculo_lado(self.origen, self.destino)
        self.perimetro = (lado1 + lado2 + lado3)








        
