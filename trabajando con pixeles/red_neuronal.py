import numpy as np
import math
import matplotlib.pyplot as plt
from probando2 import *
import random

contador = 0


def sigmoid(x):

	sig = 1 / (1 + math.exp(-x))
	return sig


class Perceptron:
	def __init__(self, capa, neurona, pesos, entradas=None, resultado=None, error=None):
		self.capa = capa
		self.neurona = neurona
		self.pesos = pesos
		self.resultado = resultado

	def sumatoria(self, entrada):
		# el cero siempre para el bias!

		#print('len entrada', len(entrada))
		z = 0  # inicializo en 0
		for i in range(len(entrada)):
			z += (entrada[i]) * self.pesos[i]

		self.resultado = sigmoid(z)

	# aca ta el errro

	def actualizar_pesos(self, lr, entrada):
		for i in range(len(entrada)):
			delta = self.error * lr * entrada[i]
			# print(delta)
			#print("paso anterior", self.pesos[i])
			self.pesos[i] += delta
			#print("paso posterior", self.pesos[i])


class RedNeuronal:
	def __init__(self, x):
		#print('creando Estructura Red Neuronal')
		self.red = []
		self.estructura = [i[0] for i in x]  # n capas ocultas
		pesos = [i[1] for i in x]

		for index, capa in enumerate(self.estructura):
			list_capa = []
			for neurona in range(capa):
				list_capa.append(Perceptron(
					index, neurona, pesos[index][neurona]))
			(self.red).append(list_capa)

	def alimentarRed(self, data):
		errorA = 1
		errorB = 1
		plt.xlabel('x')
		plt.ylabel('errores')
		plt.grid(True)
		lr = 0.1
		epochs = 0
		bias = 1
		x1 = 0
		while errorA > 0.001 and errorB > 0.001:
			print(epochs)
			for indice, dato in enumerate(data):
				#print(f'indice {indice}')  IMPORTANTE
				try:
					for indiceCapa, capa in enumerate(self.red):
						for neurona in capa:
							if neurona.capa == 0:
								# PRIMERA CAPA
								# entran mis data.shape[:-1]  --> 1 x peso!  me queda un peso. para el bias :)
								entrada = [bias] + list(dato[:-1])

							else:
								# CAPAS INTERMEDIAS
								resultados_anteriores = [
									i.resultado for i in self.red[neurona.capa - 1]]
								entrada = [bias] + resultados_anteriores

							neurona.sumatoria(entrada)

							neurona.error = dato[-1] - neurona.resultado
							error = abs(neurona.error)
							if indice % 2 == 0:
								color = 'green'
								errorA = abs(neurona.error)

							else:
								color = 'orange'
								errorB = abs(neurona.error)

							if indiceCapa == (len(self.estructura) - 1):
								
								plt.plot(x1, abs(neurona.error),"o", color=color)

							# for i in neurona.pesos:
							#   plot2.plot(x,i,".",color='black')
							x1 += 0.1
							neurona.actualizar_pesos(lr, entrada)
				except OverflowError:
					print('pass')
			# print(f'epoch #n {epochs}')
			epochs += 1
		plt.plot(x1, abs(errorA), label = "ERRORES Claudia",color='green')
		plt.plot(x1, abs(errorB), label = "ERRORES Rosario", color='orange')
		plt.legend()
		plt.show()

def pesos_random(entradas, neuronas):
	pesos = [[random.uniform(-0.01, 0.01)
			  for _ in range(entradas)] for _ in range(neuronas)]
	return pesos


if __name__ == '__main__':
	personas = manipular_imagenes('./imagenes', './modificadas/')
	# formato input [[x,y,z],[x,y,z]]
	# mi formato input deberia ser [[pixel1, pixel2 , ..., pixel 7686, 0 (A) o 1 (B)]]

	#     xor = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]])
	#red_neuronal = RedNeuronal([[3,[0.9, 0.7, 0.5],[0.3, -0.9, -1],[0.8, 0.35, 0.1]], [1, [-0.23, -0.79, 0.56, 0.6]]])

	red_neuronal = RedNeuronal([
		[100, pesos_random(7681, 100)],
		[1, pesos_random(101, 1)]
	])
	#red_neuronal = RedNeuronal()
	red_neuronal.alimentarRed(personas)


