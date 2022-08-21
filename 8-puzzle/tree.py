import numpy as np
import copy

class TreeNode: 
    def __init__(self, data, level):

        self.data = data
        # como me doy cuenta la cantidad? dependiendo el posicionamiento del espacio vacio
        self.children = []
        self.level = level
        # se ejecuta solo una vez, para q se ejecute nuevamente tendriamos q crear otro nodo!
        self.zero_position = [int(np.where(self.data == 0)[0][0]), int(np.where(self.data == 0)[1][0])]


    def possible_moves(self):

        # zonas
        # esta en la zona? se puede mover en esa coordenada 
        # puede estar en 2 - 3 - 4 zonas 

        izquierda = [[0, 1], [0,2], [1,1], [1,2], [2,1], [2,2]]
        arriba = [[1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
        derecha = [[0,0], [0,1], [1,0], [1,1], [2,0], [2,1]]
        abajo = [[0, 0], [0,1], [0,2], [1,0], [1,1], [1,2]]


        if self.zero_position in izquierda:
            board =  copy.deepcopy(self.data)
            # a donde esta el 0 le resto 1 a la columna! 
            # esto deberia crearse en el proximo nodo. 
            board[self.zero_position[0], self.zero_position[1]] = self.data[self.zero_position[0], self.zero_position[1]-1]
            board[self.zero_position[0], self.zero_position[1]-1] = 0
            self.children.append(board)
            #print(board)
            #print('izquierda')
        
        if self.zero_position in arriba:
            board =  copy.deepcopy(self.data)
            # a donde esta el 0 le resto 1 a la fila! 
            # esto deberia crearse en el proximo nodo. 
            board[self.zero_position[0], self.zero_position[1]] = self.data[self.zero_position[0]-1, self.zero_position[1]]
            board[self.zero_position[0]-1, self.zero_position[1]] = 0
            self.children.append(board)
            #print(board)
            #print('arriba')
        
        if self.zero_position in derecha:
            board =  copy.deepcopy(self.data)
            # a donde esta el 0 le sumo 1 a la columna! 
            # esto deberia crearse en el proximo nodo. 
            board[self.zero_position[0], self.zero_position[1]] = self.data[self.zero_position[0], self.zero_position[1]+1]
            board[self.zero_position[0], self.zero_position[1]+1] = 0
            self.children.append(board)
            #print(board)
            
            #print('derecha')
        
        if self.zero_position in abajo:
            board =  copy.deepcopy(self.data)
            # a donde esta el 0 le sumo 1 a la fila! 
            # esto deberia crearse en el proximo nodo. 
            board[self.zero_position[0], self.zero_position[1]] = self.data[self.zero_position[0]+1, self.zero_position[1]]
            board[self.zero_position[0]+1, self.zero_position[1]] = 0
            self.children.append(board)
            #print(board)
            #print('abajo')
        
        if self.level < 2: 
            for i in self.children:
                x = TreeNode(data=np.array(i), level=self.level+1)
                print('\n ',x.data)
                print(x.level)
                x.possible_moves()


            

if __name__ == '__main__':
    inicial = TreeNode(data=np.array([[1,2,3],[4,5,6],[7,8,0]]), level=0)    
    print(inicial.data)
    inicial.possible_moves()
