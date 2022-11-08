import copy
import random

def print_tablero(tablero):
    for i in tablero:
        print(i)
    print('-----------------------')



def move_anchura(tablero_padre):
    hijos = []
    for indice_fila,fila in enumerate(tablero_padre):
        for indice_elemento,elemento in enumerate(fila):#columna 
            if type(elemento) == str: 
                # si puede mueve y agrega a capa 
                if indice_fila - 1 >= 0:
                    #print(f'arriba')
                    tablero = copy.deepcopy(tablero_padre)
                    tablero[indice_fila-1][indice_elemento], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila - 1][indice_elemento]
                    hijos.append(tablero)
                if indice_elemento - 1 >= 0: 
                    #print(f'izquierda')
                    tablero = copy.deepcopy(tablero_padre)
                    tablero[indice_fila][indice_elemento-1], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila][indice_elemento-1]


                    hijos.append(tablero)
                if indice_fila + 1 <= 2:
                    #print(f'abajo')
                    tablero = copy.deepcopy(tablero_padre)
                    tablero[indice_fila+1][indice_elemento], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila+1][indice_elemento]

                    hijos.append(tablero)
                if indice_elemento + 1 <= 2:
                    #print(f'derecha')
                    tablero = copy.deepcopy(tablero_padre)
                    tablero[indice_fila][indice_elemento+1], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila][indice_elemento+1]
                    hijos.append(tablero)
                #print(hijos)
                return hijos

def move(tablero):
    for indice_fila,fila in enumerate(tablero):
        for indice_elemento,elemento in enumerate(fila):#columna 
            if type(elemento) == str: 
                choice = random.choice(['arriba', 'izquierda', 'abajo', 'derecha'])
                #print(f'se intentara mover a {choice}')
                if choice == 'arriba': 
                    if indice_fila - 1 >= 0:
                        tablero[indice_fila-1][indice_elemento], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila - 1][indice_elemento]
                elif choice == 'izquierda':
                    if indice_elemento - 1 >= 0: 
                        tablero[indice_fila][indice_elemento-1], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila][indice_elemento-1]
                elif choice == 'abajo':
                    if indice_fila + 1 <= 2:
                        tablero[indice_fila+1][indice_elemento], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila+1][indice_elemento]
                elif choice == 'derecha':
                    if indice_elemento + 1 <= 2:
                        tablero[indice_fila][indice_elemento+1], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila][indice_elemento+1]

                return tablero

def desordenar(tablero, movimientos):
    movimiento = 0
    while movimiento < movimientos:
        tablero = move(tablero)
        movimiento += 1
    print(f'tablero desordenado en {movimiento} movimientos')    
    return tablero


def busqueda_random(tablero_desordenado, tablero_inicial):
    movimiento = 0
    flag = True
    while flag == True:
        if tablero_desordenado == tablero_inicial:
            print(f'encontre la solucion en {movimiento} movimientos a travez de la busqueda random')
            flag = False
        else:
            move(tablero_desordenado)
            movimiento += 1


def busqueda_anchura(tablero, tablero_inicial):
    capa = 0 
    contenido_capa = [tablero]   
    movimiento = 0
    flag = True

    # algo con parentesis!
    while flag == True:
        new_capa = []
        for i in contenido_capa:
            #print(f'indice {index} - capa {capa}')
            if i == tablero_inicial:
                print(f'encontre la solucion en {movimiento} movimientos en la capa {capa} a travez de busqueda por anchura')
                flag = False
                break
            hijos = move_anchura(i)
            movimiento += 1 
            new_capa += hijos
        
        contenido_capa = new_capa
        capa += 1

        


if __name__ == '__main__':
    tablero_inicial = [[1,2,3],[4,5,6],[7,8,'x']]
    print(tablero_inicial)
    tablero = copy.deepcopy(tablero_inicial)
    tablero_desordenado = desordenar(tablero, 10)
    print(tablero_desordenado)

    # encontre la solucion en 851304 movimientos

    busqueda_anchura(copy.deepcopy(tablero_desordenado), tablero_inicial)
    busqueda_random(copy.deepcopy(tablero_desordenado), tablero_inicial)
    

