from punto import *
from math import sqrt

class Camino:

        def __init__(self, p1,p2):
            self.origen = p1
            self.destino = p2
            self.dist_total = 0
            self.dist_p_final = 0

        def calculo_distancia_total(self, acumulado, p1, p2):   
            valor = acumulado + p1.calcular_distancia(p2)
            return valor

        def calculo_distancia_final(self, p1, p2):   
            valor = p1.calcular_distancia(p2)
            return valor
