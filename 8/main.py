import copy


def move(tablero):
    for indice_fila,fila in enumerate(tablero):
        for indice_elemento,elemento in enumerate(fila):#columna 
            if type(elemento) == str: 
                if indice_fila - 1 >= 0:
                    tablero[indice_fila-1][indice_elemento], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila - 1][indice_elemento]
                    print('arriba')
                if indice_elemento - 1 >= 0: 
                    tablero[indice_fila][indice_elemento-1], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila][indice_elemento-1]
                    print('izquierda')

                if indice_fila + 1 <= 2:
                    tablero[indice_fila+1][indice_elemento], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila + 1][indice_elemento]
                    print('abajo')

                if indice_elemento + 1 <= 2:
                    tablero[indice_fila][indice_elemento+1], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila][indice_elemento+1]
                    print('derecha')



def desordenar(tablero):
    print(tablero)
    movimiento = 0
    while movimiento < 50:
        move(tablero)
        movimiento += 1
    print(f'tablero desordenado en {movimiento} movimientos\n{tablero}')
    return tablero


def busqueda_random(tablero_desordenado, tablero_inicial):
    movimiento = 0
    flag = True
    while flag == True:
        if tablero_desordenado == tablero_inicial:
            print(f'eureka {tablero_desordenado} \n{tablero_inicial}')
            print(f'encontre la solucion en {movimiento} movimientos')
            flag = False
        else:
            move(tablero_desordenado)



if __name__ == '__main__':
    tablero_inicial = [[1,2,3],[4,5,6],[7,8,'x']]
    tablero = copy.deepcopy(tablero_inicial)
    tablero_desordenado = desordenar(tablero)

    #busqueda_random(tablero_desordenado, tablero_inicial)  #no anda. 

    print(tablero_inicial)