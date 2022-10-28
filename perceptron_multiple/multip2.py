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
        self.entradas = entradas


    def sumatoria(self, entrada):
        print(f'\nsumatoria! entrada: {entrada}  lenght {len(entrada)}')
        # el cero siempre para el bias!
        z = 0 # inicializo en 0
        for i in range(len(entrada)):
            z += entrada[i] * self.pesos[i]
        print(z)
        self.resultado = sigmoid(z)
        print(self.resultado)

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
        bias = 1
        print('\n\n\noperamos con el dato ', data, '\n\n')
        for capa in self.red: 
            for neurona in capa:
                if neurona.capa == 0:
                    #PRIMERA CAPA
                    # entran mis data.shape[:-1]  --> 1 x peso!  me queda un peso. para el bias :)
                    print(f"\ncapa {neurona.capa} neurona {neurona.neurona} pesos {neurona.pesos} ")
                    neurona.entradas = [bias] + list(data[:-1])
                    neurona.sumatoria(neurona.entradas)
                else: 
                    # CAPAS INTERMEDIAS
                    resultados_anteriores = [i.resultado for i in self.red[neurona.capa - 1]]
                    print(f"capa {neurona.capa} neurona {neurona.neurona} pesos {neurona.pesos} ")
                    print(f'resultados capa anterior {resultados_anteriores}')
                    neurona.entradas = [bias] + resultados_anteriores
                    neurona.sumatoria(neurona.entradas)
    def backpropagation(self, data):
        for indice, capa in enumerate(reversed(self.red)):
            salida_deseada = data
            
            for neurona in capa:
                salida_real = neurona.resultado
                if indice == 0: 
                    e = salida_deseada - salida_real
                    deltaf = salida_real * (1 - salida_real) * e
                    print('delta f ', deltaf)
                    print(type(deltaf))
                    for indice, entrada in enumerate(neurona.entradas):
                        neurona.pesos[indice] = 0.1 * entrada * deltaf
                else: 
                    pass




                print(indice, capa)
if __name__ == '__main__':

    xor = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]])
    red_neuronal = RedNeuronal([[3,[0.9, 0.7, 0.5],[0.3, -0.9, -1],[0.8, 0.35, 0.1]], [1, [-0.23, -0.79, 0.56, 0.6]]])
    #for i in xor:
    #    red_neuronal.alimentarRed(i)   #ida
    #    red_neuronal.backpropagation(i) #vuelta

    red_neuronal.alimentarRed(xor[0])
    red_neuronal.backpropagation(xor[0])

    # backpropagation
    # sd salida deseada -  sr salida real 
    # salida deseada = xor --> solo la se en la ultima capa
    # e = Sd - Sr
    # gf = Sr * (1 - Sr) * e 
    # delta w = LR(0.1) * ent * gf

    # agarro la ultima capa
    #ultima_capa = red_neuronal.red[-1]
    # ultima_capa[0] tengo solo un obj perceptron en esa capa
    #print(ultima_capa[0])
    #print("neurona ", ultima_capa[0].neurona)
    #print("entradas ", ultima_capa[0].entradas)
    #print("pesos ", ultima_capa[0].pesos)
    #print("resultado ", ultima_capa[0].resultado)
