from math import sqrt

class Punto_forma:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calcular_distancia(self ,punto):
        distancia = sqrt((self.x - punto.x)**2+(self.y - punto.y)**2)
        return distancia
