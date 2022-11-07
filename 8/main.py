

def desordenar(tablero):
    print(tablero)
    movimiento = 0
    while movimiento < 50:
        for indice_fila,fila in enumerate(tablero):
            for indice_elemento,elemento in enumerate(fila):#columna 
                if type(elemento) == str: 
                    #indice = (indice_fila, indice_elemento)
                    if indice_fila - 1 >= 0:
                        # se puede mover para arriba
                        tablero[indice_fila-1][indice_elemento], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila - 1][indice_elemento]
                        print('arriba')
                        movimiento += 1
                    if indice_elemento - 1 >= 0: 
                        # no se puede mover para arriba pero si para la izq
                        tablero[indice_fila][indice_elemento-1], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila][indice_elemento-1]
                        print('izquierda')
                        movimiento += 1

                    if indice_fila + 1 <= 2:
                        # si indice_fila fuese 2 (ultima columna) 2+1=3 no seria ni menor ni igual a 2 - no se podria
                        # no se puede mover para arriba ni para la izquierda pero si para abajo

                        # si le sumo uno  a la fila es menor o igual al numero de filas total
                        tablero[indice_fila+1][indice_elemento], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila + 1][indice_elemento]
                        print('abajo')
                        movimiento += 1

                    if indice_elemento + 1 <= 2:
                        tablero[indice_fila][indice_elemento+1], tablero[indice_fila][indice_elemento] = tablero[indice_fila][indice_elemento], tablero[indice_fila][indice_elemento+1]
                        print('derecha')
                        movimiento += 1
    
    print(f'tablero desordenado en {movimiento} movimientos\n{tablero}')
    return tablero





if __name__ == '__main__':
    tablero_inicial = [[1,2,3],[4,5,6],[7,8,'x']]
    tablero_desordenado = desordenar(tablero_inicial)