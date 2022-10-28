import numpy as np
import math
import matplotlib.pyplot as plt


def sigmoid(x):
	sig = 1 / (1 + math.exp(-x))
	return sig

class Perceptron: 
    def __init__(self, capa, neurona, pesos, entradas=None, resultado=None, error=None):
        #print('creando neurona')
        self.capa = capa
        self.neurona = neurona
        self.pesos = pesos
        self.resultado =  resultado

    def sumatoria(self, entrada):
        #print(f'\nsumatoria! entrada: {entrada}  lenght {len(entrada)}')
        # el cero siempre para el bias!
        z = 0 # inicializo en 0
    
        for i in range(len(entrada)):
            z += entrada[i] * self.pesos[i]
        #print("z", z)
        #print("sigmoide ", sigmoid(z))
        self.resultado = sigmoid(z)

    #aca ta el errro
    def actualizar_pesos(self, lr, entrada):
        for i in range(len(entrada)):
            delta = self.error * lr * entrada[i]
            #print(delta)
            #print("paso anterior", self.pesos[i])
            self.pesos[i] += delta
            #print("paso posterior", self.pesos[i])

class RedNeuronal:
    def __init__(self, x):
        #print('creando Estructura Red Neuronal')
        self.red = []
        self.estructura = [i[0] for i in x] # n capas ocultas 
        pesos = [i[1:] for i in x]
        for index, capa in enumerate(self.estructura): 
            list_capa = []
            for neurona in range(capa):
                list_capa.append(Perceptron(index, neurona, pesos[index][neurona]))
            (self.red).append(list_capa)
    
    def alimentarRed(self, data):

        lr = 0.5
        epochs = 0
        bias = 1
        colors = ['green', 'red', 'black', 'yellow']
        x = 0

        print(len(self.estructura))
        while epochs < 1000:

            for indice, dato in enumerate(data):
                #print(f'{indice, dato}')
                
                for indiceCapa, capa in enumerate(self.red): 
                    for neurona in capa:
                        if neurona.capa == 0:
                            #PRIMERA CAPA
                            # entran mis data.shape[:-1]  --> 1 x peso!  me queda un peso. para el bias :)
                            entrada = [bias] + list(dato[:-1])

                        else: 
                            # CAPAS INTERMEDIAS
                            resultados_anteriores = [i.resultado for i in self.red[neurona.capa - 1]]
                            entrada = [bias] + resultados_anteriores
                            
                        neurona.sumatoria(entrada)
                        #print(dato[-1], neurona.resultado)
                        neurona.error = dato[-1] - neurona.resultado
                        #print('error', neurona.error)
                        if indiceCapa == (len(self.estructura) - 1):
                            plt.plot(x,abs(neurona.error),"o",color=colors[indice])
                        x += 0.1
                        neurona.actualizar_pesos(lr, entrada)
            #print(f'epoch #n {epochs}')
            epochs += 1
if __name__ == '__main__':

    xor = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]])
    try:
        red_neuronal = RedNeuronal([[2, [0.9, 0.7, 0.5], [0.3, -0.9, -1]], [3, [0.8, 0.35, 0.1], [-0.23, -0.79, 0.56], [0.6, -0.6, 0.22]], [1, [-0.22, -0.55, 0.31, -0.32]]])

        red_neuronal.alimentarRed(xor)
        plt.show()
    except IndexError:
        print("Has propocionado mal la estructura de la red neuronal!")
