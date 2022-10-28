import numpy as np
import math

def sigmoid(x):
	sig = 1 / (1 + math.exp(-x))
	return sig

class Perceptron: 
    def __init__(self, capa, neurona, pesos, entradas=None, resultado=None):
        print('creando neurona')
        self.capa = capa
        self.neurona = neurona
        self.pesos = pesos
        self.resultado =  resultado

    def sumatoria(self, entrada):
        print(f'\nsumatoria! entrada: {entrada}  lenght {len(entrada)}')
        # el cero siempre para el bias!
        z = 0 # inicializo en 0

        for i in range(len(entrada)):
            z += entrada[i] * self.pesos[i]
        self.resultado = sigmoid(z)
        print('self.resultado', self.resultado)


class RedNeuronal:
    def __init__(self, x):
        print('creando Estructura Red Neuronal')
        self.red = []
        estructura = [i[0] for i in x]
        pesos = [i[1:] for i in x]
        for index, capa in enumerate(estructura): 
            list_capa = []
            for neurona in range(capa):
                list_capa.append(Perceptron(index, neurona, pesos[index][neurona]))
            (self.red).append(list_capa)
    
    def alimentarRed(self, data):
        # data : xor!
        print(f"filas -> muestras : {data.shape[0]}")
        # data.shape - 1 = lo que "entra en las primeras neuronas" y ultima fila el y !! lo q deberia obtener 
        print(f"columnas -> variables y ultima fila resultado ... {data.shape[1]}")
        bias = 1
        for dato in data:
            print('\n\n\noperamos con el dato ', dato, '\n\n')
            for capa in self.red: 
                for neurona in capa:
                    if neurona.capa == 0:
                        #PRIMERA CAPA
                        # entran mis data.shape[:-1]  --> 1 x peso!  me queda un peso. para el bias :)
                        print(f"\ncapa {neurona.capa} neurona {neurona.neurona} pesos {neurona.pesos} ")
                        entrada = [bias] + list(dato[:-1])
                        neurona.sumatoria(entrada)
                    else: 
                        # CAPAS INTERMEDIAS
                        resultados_anteriores = [i.resultado for i in self.red[neurona.capa - 1]]
                        print(f"capa {neurona.capa} neurona {neurona.neurona} pesos {neurona.pesos} ")
                        print(f'resultados capa anterior {resultados_anteriores}')
                        entrada = [bias] + resultados_anteriores
                        neurona.sumatoria(entrada)


if __name__ == '__main__':

    xor = np.array([[0, 0, 0]])
    red_neuronal = RedNeuronal([[2, [0.9, 0.7, 0.5], [0.3, -0.9, -1]], [3, [0.8, 0.35, 0.1], [-0.23, -0.79, 0.56], [0.6, -0.6, 0.22]], [1, [-0.22, -0.55, 0.31, -0.32]]])
    red_neuronal.alimentarRed(xor)
