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
    As=0
    for i in range (0,len(lista)):
        if 'A' == lista [i][0] :
            lista [i] = (1,lista [i][1])
            As=1
            break
    return lista,As

def cambio_As (lista):
    print(lista)
    print (str(suma(lista)))
    res = suma(lista)
    while res>21:
        lista_carta, As = buscar_As(lista)
        res = suma(lista)
        if As==0:
            break
    print(lista)
    print (str(suma(lista)))
    return lista,res

def carta_ini(lista_carta, lista):
    aleatorio1,aleatorio2 = aleatorio(len(lista)),aleatorio(len(lista))
    lista_carta.append(lista.pop(aleatorio1))
    lista_carta.append(lista.pop(aleatorio2))
    return lista_carta, lista
    
            
lista = [(v, p) for v in ['A','2','3','4','5','6','7','8','9','j','q','k'] for p in ['c','d','p','t']]

lista_carta = []
lista_maquina = []

lista_carta, lista =carta_ini(lista_carta, lista)
jugador=0

while True :
    lista_carta, res=cambio_As(lista_carta)
    if res<=21:
        u= input('quiere otra carta s/ :')
        if u == 's' :

            lista_carta.append(lista.pop(aleatorio(len(lista))))
        else :
            lista_maquina, lista =carta_ini(lista_maquina, lista)
            while True:
                lista_maquina, mres=cambio_As(lista_maquina)
                if mres<=21 and mres<res:
                    lista_maquina.append(lista.pop(aleatorio(len(lista))))
                else:
                    if mres>=res and mres<22:
                        print('puntaje del jugador: ' + str(res))
                        print('puntaje de la maquina: ' + str(mres))
                        print('la maquina gana')
                    else:
                        print('puntaje del jugador: ' + str(res))
                        print('puntaje de la maquina: ' + str(mres))
                        print('el jugador gana')
                    break
            break
    else:
        print('el jugador pierde su puntaje es mayor a 21')

        break
