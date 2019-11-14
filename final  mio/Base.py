from final1 import *


p=[(0,5),(0,10),(0,11),(0,13),(0,15),(0,18)]

lista=[]
dist_final=[]
dist_total=[]
lista_t=[]

num_puntos=len(p)

for i in range(num_puntos):
    lista.append(Punto_forma(p[i][0],p[i][1]))
dist_min=0
acum=0;
for i in range(num_puntos-1):
    c=Camino(lista[i],lista[i+1])
    #calculo distancia con el punto final
    dist_final.append(c.calculo_distancia_final(lista[i],lista[num_puntos-1]))
    dist_total.append(c.calculo_distancia_total(acum,lista[i],lista[i+1]))
    acum=dist_total[i]

    print('dist_final :' + str(dist_final[i]))
    print('dist_total :' + str(dist_total[i]))
    temp=[p[i], dist_final[i], dist_total[i]]
    lista_t.append(temp)
    if i!= 0:
        if dist_min>dist_final[i]:
            dist_min=dist_final[i]
    else:
        dist_min=dist_final[0]
    
    

print('dist_min :' + str(dist_min))
print('dist_min :' + str(dist_min))

'''  
for i in range(numero_puntos):
    print(p[i])
  
cuadrado.calcular_area()
cuadrado.calcular_perimetro()




'''
