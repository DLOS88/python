import random
def valor_carta (c):
    if c == "j" :
        return 10
    elif c == 'q' :
        return 10
    elif c == 'k' :
        return 10
    elif c == 'A' :
        return 11
    else :
        return c
    
def suma (lista):
    total=0
    for i in range(0,len(lista)):
        total += int (valor_carta(lista[i][0]))
    return total
    
def aleatorio (tlist) :
    return random.randint(0,tlist-1)


def buscar_As (lista):
    for i in range (0,len(lista)):
        if 'A' == lista [i][0] :
            lista [i] = (1,lista [i][1])
            break
    return lista
            
lista = [(v, p) for v in ['A','2','3','4','5','6','7','8','9','j','q','k'] for p in ['c','d','p','t']]
aleatorio1,aleatorio2 = aleatorio(len(lista)),aleatorio(len(lista))
lista_carta = []

lista_carta.append(lista.pop(aleatorio1))
lista_carta.append(lista.pop(aleatorio2))

while True :
    print(lista_carta)
    print (str(suma(lista_carta)))
    res = suma(lista_carta)
    while res>21 :
        lista_carta = buscar_As(lista_carta)
        print (str(suma(lista_carta)))
        res = suma(lista_carta)
    u= input('quiere otra carta s/n :')
    if u == 's' :

        lista_carta.append(lista.pop(aleatorio(len(lista))))
    else :
        break

        
        








